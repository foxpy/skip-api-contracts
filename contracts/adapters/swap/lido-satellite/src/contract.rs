use crate::{
    error::{ContractError, ContractResult},
    state::{ENTRY_POINT_CONTRACT_ADDRESS, LIDO_SATELLITE_CONTRACT_ADDRESS},
};
use cosmwasm_std::{entry_point, to_binary, DepsMut, Env, MessageInfo, Response, WasmMsg};
use cw_utils::one_coin;
use skip::swap::{
    execute_transfer_funds_back, ExecuteMsg, LidoSatelliteInstantiateMsg as InstantiateMsg,
    SwapOperation,
};

///////////////////
/// INSTANTIATE ///
///////////////////

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    _info: MessageInfo,
    msg: InstantiateMsg,
) -> ContractResult<Response> {
    // Validate entry point contract address
    let checked_entry_point_contract_address =
        deps.api.addr_validate(&msg.entry_point_contract_address)?;

    // Store the entry point contract address
    ENTRY_POINT_CONTRACT_ADDRESS.save(deps.storage, &checked_entry_point_contract_address)?;

    // Validate satellite contract address
    let checked_lido_satellite_contract_address = deps
        .api
        .addr_validate(&msg.lido_satellite_contract_address)?;

    // Store the satellite contract address
    LIDO_SATELLITE_CONTRACT_ADDRESS.save(deps.storage, &checked_lido_satellite_contract_address)?;

    Ok(Response::new()
        .add_attribute("action", "instantiate")
        .add_attribute(
            "entry_point_contract_address",
            checked_entry_point_contract_address.to_string(),
        )
        .add_attribute(
            "lido_satellite_contract_address",
            checked_lido_satellite_contract_address.to_string(),
        ))
}

///////////////
/// EXECUTE ///
///////////////

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn execute(
    deps: DepsMut,
    env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> ContractResult<Response> {
    match msg {
        ExecuteMsg::Swap { operations } => execute_swap(deps, env, info, operations),
        ExecuteMsg::TransferFundsBack { swapper } => {
            Ok(execute_transfer_funds_back(deps, env, info, swapper)?)
        }
    }
}

fn execute_swap(
    deps: DepsMut,
    env: Env,
    info: MessageInfo,
    // FIXME: seems like we are doomed to ignore this field at all?
    _operations: Vec<SwapOperation>,
) -> ContractResult<Response> {
    // Get entry point contract address from storage
    let entry_point_contract_address = ENTRY_POINT_CONTRACT_ADDRESS.load(deps.storage)?;

    // Enforce the caller is the entry point contract
    if info.sender != entry_point_contract_address {
        return Err(ContractError::Unauthorized);
    }

    // Get coin in from the message info, error if there is not exactly one coin sent
    let coin_in = one_coin(&info)?;

    // TODO: we should probably check that provided coin equals to bridged_denom from
    //       Lido Satellite config. But it is not a big problem since Lido Satellite
    //       performs such a check anyway.

    let lido_satellite_contract_address = LIDO_SATELLITE_CONTRACT_ADDRESS.load(deps.storage)?;
    let mint_msg = lido_satellite::msg::ExecuteMsg::Mint { receiver: None };

    let swap_msg = WasmMsg::Execute {
        contract_addr: lido_satellite_contract_address.to_string(),
        msg: to_binary(&mint_msg)?,
        funds: vec![coin_in],
    };

    // Create the transfer funds back message
    let transfer_funds_back_msg = WasmMsg::Execute {
        contract_addr: env.contract.address.to_string(),
        msg: to_binary(&ExecuteMsg::TransferFundsBack {
            swapper: info.sender,
        })?,
        funds: vec![],
    };

    Ok(Response::new()
        .add_message(swap_msg)
        .add_message(transfer_funds_back_msg)
        .add_attribute("action", "dispatch_swap_and_transfer_back"))
}
