use cosmwasm_schema::write_api;
use skip::swap::{ExecuteMsg, NeutronInstantiateMsg as InstantiateMsg, QueryMsg};

fn main() {
    write_api! {
        instantiate: InstantiateMsg,
        execute: ExecuteMsg,
        query: QueryMsg
    }
}
