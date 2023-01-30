# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from arista.redirector.v1.services import gen_pb2 as arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2


class AssignmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOne = channel.unary_unary(
                '/arista.redirector.v1.AssignmentService/GetOne',
                request_serializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentRequest.SerializeToString,
                response_deserializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentResponse.FromString,
                )
        self.GetAll = channel.unary_stream(
                '/arista.redirector.v1.AssignmentService/GetAll',
                request_serializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamRequest.SerializeToString,
                response_deserializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/arista.redirector.v1.AssignmentService/Subscribe',
                request_serializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamRequest.SerializeToString,
                response_deserializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamResponse.FromString,
                )


class AssignmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AssignmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOne': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOne,
                    request_deserializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentRequest.FromString,
                    response_serializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentResponse.SerializeToString,
            ),
            'GetAll': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamRequest.FromString,
                    response_serializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamRequest.FromString,
                    response_serializer=arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arista.redirector.v1.AssignmentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AssignmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arista.redirector.v1.AssignmentService/GetOne',
            arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentRequest.SerializeToString,
            arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/arista.redirector.v1.AssignmentService/GetAll',
            arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamRequest.SerializeToString,
            arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/arista.redirector.v1.AssignmentService/Subscribe',
            arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamRequest.SerializeToString,
            arista_dot_redirector_dot_v1_dot_services_dot_gen__pb2.AssignmentStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
