

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transaction_pb2 as transaction__pb2


class TransactionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendMoney = channel.unary_unary(
                '/TransactionService/sendMoney',
                request_serializer=transaction__pb2.TransactionRequest.SerializeToString,
                response_deserializer=transaction__pb2.TransactionResponse.FromString,
                )
        self.getTransactionsHistory = channel.unary_unary(
                '/TransactionService/getTransactionsHistory',
                request_serializer=transaction__pb2.GetALLTransactionsRequest.SerializeToString,
                response_deserializer=transaction__pb2.GetALLTransactionsResponse.FromString,
                )
        self.Zelle = channel.unary_unary(
                '/TransactionService/Zelle',
                request_serializer=transaction__pb2.ZelleRequest.SerializeToString,
                response_deserializer=transaction__pb2.TransactionResponse.FromString,
                )
        self.getTransactionByID = channel.unary_unary(
                '/TransactionService/getTransactionByID',
                request_serializer=transaction__pb2.TransactionByIDRequest.SerializeToString,
                response_deserializer=transaction__pb2.Transaction.FromString,
                )


class TransactionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendMoney(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTransactionsHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Zelle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTransactionByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendMoney': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMoney,
                    request_deserializer=transaction__pb2.TransactionRequest.FromString,
                    response_serializer=transaction__pb2.TransactionResponse.SerializeToString,
            ),
            'getTransactionsHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.getTransactionsHistory,
                    request_deserializer=transaction__pb2.GetALLTransactionsRequest.FromString,
                    response_serializer=transaction__pb2.GetALLTransactionsResponse.SerializeToString,
            ),
            'Zelle': grpc.unary_unary_rpc_method_handler(
                    servicer.Zelle,
                    request_deserializer=transaction__pb2.ZelleRequest.FromString,
                    response_serializer=transaction__pb2.TransactionResponse.SerializeToString,
            ),
            'getTransactionByID': grpc.unary_unary_rpc_method_handler(
                    servicer.getTransactionByID,
                    request_deserializer=transaction__pb2.TransactionByIDRequest.FromString,
                    response_serializer=transaction__pb2.Transaction.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TransactionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransactionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendMoney(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TransactionService/sendMoney',
            transaction__pb2.TransactionRequest.SerializeToString,
            transaction__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTransactionsHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TransactionService/getTransactionsHistory',
            transaction__pb2.GetALLTransactionsRequest.SerializeToString,
            transaction__pb2.GetALLTransactionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Zelle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TransactionService/Zelle',
            transaction__pb2.ZelleRequest.SerializeToString,
            transaction__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTransactionByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TransactionService/getTransactionByID',
            transaction__pb2.TransactionByIDRequest.SerializeToString,
            transaction__pb2.Transaction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)