# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from arista.alert.v1.services import gen_pb2 as arista_dot_alert_dot_v1_dot_services_dot_gen__pb2


class AlertServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOne = channel.unary_unary(
                '/arista.alert.v1.AlertService/GetOne',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/arista.alert.v1.AlertService/Subscribe',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertStreamRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertStreamResponse.FromString,
                )


class AlertServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOne': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOne,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertStreamRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arista.alert.v1.AlertService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AlertService(object):
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
        return grpc.experimental.unary_unary(request, target, '/arista.alert.v1.AlertService/GetOne',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertResponse.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/arista.alert.v1.AlertService/Subscribe',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertStreamRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AlertConfigServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOne = channel.unary_unary(
                '/arista.alert.v1.AlertConfigService/GetOne',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/arista.alert.v1.AlertConfigService/Subscribe',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigStreamRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigStreamResponse.FromString,
                )
        self.Set = channel.unary_unary(
                '/arista.alert.v1.AlertConfigService/Set',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigSetRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigSetResponse.FromString,
                )


class AlertConfigServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertConfigServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOne': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOne,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigStreamRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigStreamResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigSetRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigSetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arista.alert.v1.AlertConfigService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AlertConfigService(object):
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
        return grpc.experimental.unary_unary(request, target, '/arista.alert.v1.AlertConfigService/GetOne',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigResponse.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/arista.alert.v1.AlertConfigService/Subscribe',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigStreamRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arista.alert.v1.AlertConfigService/Set',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigSetRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.AlertConfigSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TemplateConfigServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOne = channel.unary_unary(
                '/arista.alert.v1.TemplateConfigService/GetOne',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigResponse.FromString,
                )
        self.GetAll = channel.unary_stream(
                '/arista.alert.v1.TemplateConfigService/GetAll',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/arista.alert.v1.TemplateConfigService/Subscribe',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamResponse.FromString,
                )
        self.Set = channel.unary_unary(
                '/arista.alert.v1.TemplateConfigService/Set',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetResponse.FromString,
                )
        self.SetSome = channel.unary_stream(
                '/arista.alert.v1.TemplateConfigService/SetSome',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetSomeRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetSomeResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/arista.alert.v1.TemplateConfigService/Delete',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteResponse.FromString,
                )
        self.DeleteAll = channel.unary_stream(
                '/arista.alert.v1.TemplateConfigService/DeleteAll',
                request_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteAllRequest.SerializeToString,
                response_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteAllResponse.FromString,
                )


class TemplateConfigServiceServicer(object):
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

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSome(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TemplateConfigServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOne': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOne,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigResponse.SerializeToString,
            ),
            'GetAll': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamResponse.SerializeToString,
            ),
            'Set': grpc.unary_unary_rpc_method_handler(
                    servicer.Set,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetResponse.SerializeToString,
            ),
            'SetSome': grpc.unary_stream_rpc_method_handler(
                    servicer.SetSome,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetSomeRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetSomeResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_stream_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteAllRequest.FromString,
                    response_serializer=arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteAllResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arista.alert.v1.TemplateConfigService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TemplateConfigService(object):
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
        return grpc.experimental.unary_unary(request, target, '/arista.alert.v1.TemplateConfigService/GetOne',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigResponse.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/arista.alert.v1.TemplateConfigService/GetAll',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamResponse.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/arista.alert.v1.TemplateConfigService/Subscribe',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arista.alert.v1.TemplateConfigService/Set',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSome(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/arista.alert.v1.TemplateConfigService/SetSome',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetSomeRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigSetSomeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arista.alert.v1.TemplateConfigService/Delete',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/arista.alert.v1.TemplateConfigService/DeleteAll',
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteAllRequest.SerializeToString,
            arista_dot_alert_dot_v1_dot_services_dot_gen__pb2.TemplateConfigDeleteAllResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
