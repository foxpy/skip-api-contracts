"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmwasm.wasm.v1 import query_pb2 as cosmwasm_dot_wasm_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query provides defines the gRPC querier service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ContractInfo = channel.unary_unary('/cosmwasm.wasm.v1.Query/ContractInfo', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractInfoRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractInfoResponse.FromString)
        self.ContractHistory = channel.unary_unary('/cosmwasm.wasm.v1.Query/ContractHistory', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractHistoryRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractHistoryResponse.FromString)
        self.ContractsByCode = channel.unary_unary('/cosmwasm.wasm.v1.Query/ContractsByCode', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCodeRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCodeResponse.FromString)
        self.AllContractState = channel.unary_unary('/cosmwasm.wasm.v1.Query/AllContractState', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryAllContractStateRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryAllContractStateResponse.FromString)
        self.RawContractState = channel.unary_unary('/cosmwasm.wasm.v1.Query/RawContractState', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryRawContractStateRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryRawContractStateResponse.FromString)
        self.SmartContractState = channel.unary_unary('/cosmwasm.wasm.v1.Query/SmartContractState', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QuerySmartContractStateRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QuerySmartContractStateResponse.FromString)
        self.Code = channel.unary_unary('/cosmwasm.wasm.v1.Query/Code', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodeRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodeResponse.FromString)
        self.Codes = channel.unary_unary('/cosmwasm.wasm.v1.Query/Codes', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodesRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodesResponse.FromString)
        self.PinnedCodes = channel.unary_unary('/cosmwasm.wasm.v1.Query/PinnedCodes', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryPinnedCodesRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryPinnedCodesResponse.FromString)
        self.Params = channel.unary_unary('/cosmwasm.wasm.v1.Query/Params', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.ContractsByCreator = channel.unary_unary('/cosmwasm.wasm.v1.Query/ContractsByCreator', request_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCreatorRequest.SerializeToString, response_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCreatorResponse.FromString)

class QueryServicer(object):
    """Query provides defines the gRPC querier service
    """

    def ContractInfo(self, request, context):
        """ContractInfo gets the contract meta data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractHistory(self, request, context):
        """ContractHistory gets the contract code history
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractsByCode(self, request, context):
        """ContractsByCode lists all smart contracts for a code id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllContractState(self, request, context):
        """AllContractState gets all raw store data for a single contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RawContractState(self, request, context):
        """RawContractState gets single key from the raw store data of a contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SmartContractState(self, request, context):
        """SmartContractState get smart query result from the contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Code(self, request, context):
        """Code gets the binary code and metadata for a singe wasm code
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Codes(self, request, context):
        """Codes gets the metadata for all stored wasm codes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PinnedCodes(self, request, context):
        """PinnedCodes gets the pinned code ids
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params gets the module params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractsByCreator(self, request, context):
        """ContractsByCreator gets the contracts by creator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ContractInfo': grpc.unary_unary_rpc_method_handler(servicer.ContractInfo, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractInfoRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractInfoResponse.SerializeToString), 'ContractHistory': grpc.unary_unary_rpc_method_handler(servicer.ContractHistory, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractHistoryRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractHistoryResponse.SerializeToString), 'ContractsByCode': grpc.unary_unary_rpc_method_handler(servicer.ContractsByCode, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCodeRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCodeResponse.SerializeToString), 'AllContractState': grpc.unary_unary_rpc_method_handler(servicer.AllContractState, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryAllContractStateRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryAllContractStateResponse.SerializeToString), 'RawContractState': grpc.unary_unary_rpc_method_handler(servicer.RawContractState, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryRawContractStateRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryRawContractStateResponse.SerializeToString), 'SmartContractState': grpc.unary_unary_rpc_method_handler(servicer.SmartContractState, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QuerySmartContractStateRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QuerySmartContractStateResponse.SerializeToString), 'Code': grpc.unary_unary_rpc_method_handler(servicer.Code, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodeRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodeResponse.SerializeToString), 'Codes': grpc.unary_unary_rpc_method_handler(servicer.Codes, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodesRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodesResponse.SerializeToString), 'PinnedCodes': grpc.unary_unary_rpc_method_handler(servicer.PinnedCodes, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryPinnedCodesRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryPinnedCodesResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'ContractsByCreator': grpc.unary_unary_rpc_method_handler(servicer.ContractsByCreator, request_deserializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCreatorRequest.FromString, response_serializer=cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCreatorResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmwasm.wasm.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query provides defines the gRPC querier service
    """

    @staticmethod
    def ContractInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/ContractInfo', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractInfoRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContractHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/ContractHistory', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractHistoryRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractHistoryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContractsByCode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/ContractsByCode', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCodeRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllContractState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/AllContractState', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryAllContractStateRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryAllContractStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RawContractState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/RawContractState', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryRawContractStateRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryRawContractStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SmartContractState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/SmartContractState', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QuerySmartContractStateRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QuerySmartContractStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Code(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/Code', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodeRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Codes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/Codes', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodesRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryCodesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PinnedCodes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/PinnedCodes', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryPinnedCodesRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryPinnedCodesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/Params', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContractsByCreator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmwasm.wasm.v1.Query/ContractsByCreator', cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCreatorRequest.SerializeToString, cosmwasm_dot_wasm_dot_v1_dot_query__pb2.QueryContractsByCreatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)