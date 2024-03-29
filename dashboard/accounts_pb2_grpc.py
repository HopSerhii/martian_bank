

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import accounts_pb2 as accounts__pb2


class AccountDetailsServiceStub(object):
    """message GetAccountDetailResponse {
    AccountDetail account = 1;
    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getAccountDetails = channel.unary_unary(
                '/AccountDetailsService/getAccountDetails',
                request_serializer=accounts__pb2.GetAccountDetailRequest.SerializeToString,
                response_deserializer=accounts__pb2.AccountDetail.FromString,
                )
        self.createAccount = channel.unary_unary(
                '/AccountDetailsService/createAccount',
                request_serializer=accounts__pb2.CreateAccountRequest.SerializeToString,
                response_deserializer=accounts__pb2.CreateAccountResponse.FromString,
                )
        self.getAccounts = channel.unary_unary(
                '/AccountDetailsService/getAccounts',
                request_serializer=accounts__pb2.GetAccountsRequest.SerializeToString,
                response_deserializer=accounts__pb2.GetAccountsResponse.FromString,
                )


class AccountDetailsServiceServicer(object):
    """message GetAccountDetailResponse {
    AccountDetail account = 1;
    }

    """

    def getAccountDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAccounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountDetailsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getAccountDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.getAccountDetails,
                    request_deserializer=accounts__pb2.GetAccountDetailRequest.FromString,
                    response_serializer=accounts__pb2.AccountDetail.SerializeToString,
            ),
            'createAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.createAccount,
                    request_deserializer=accounts__pb2.CreateAccountRequest.FromString,
                    response_serializer=accounts__pb2.CreateAccountResponse.SerializeToString,
            ),
            'getAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.getAccounts,
                    request_deserializer=accounts__pb2.GetAccountsRequest.FromString,
                    response_serializer=accounts__pb2.GetAccountsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AccountDetailsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountDetailsService(object):
    """message GetAccountDetailResponse {
    AccountDetail account = 1;
    }

    """

    @staticmethod
    def getAccountDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AccountDetailsService/getAccountDetails',
            accounts__pb2.GetAccountDetailRequest.SerializeToString,
            accounts__pb2.AccountDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AccountDetailsService/createAccount',
            accounts__pb2.CreateAccountRequest.SerializeToString,
            accounts__pb2.CreateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AccountDetailsService/getAccounts',
            accounts__pb2.GetAccountsRequest.SerializeToString,
            accounts__pb2.GetAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
