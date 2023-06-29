# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fmp/yang.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fmp/yang.proto',
  package='fmp',
  syntax='proto3',
  serialized_options=b'Z0github.com/aristanetworks/cloudvision-go/api/fmp',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x66mp/yang.proto\x12\x03\x66mp\"\x1b\n\nMACAddress\x12\r\n\x05value\x18\x01 \x01(\t\"5\n\x12RepeatedMACAddress\x12\x1f\n\x06values\x18\x01 \x03(\x0b\x32\x0f.fmp.MACAddressB2Z0github.com/aristanetworks/cloudvision-go/api/fmpb\x06proto3'
)




_MACADDRESS = _descriptor.Descriptor(
  name='MACAddress',
  full_name='fmp.MACAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='fmp.MACAddress.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=50,
)


_REPEATEDMACADDRESS = _descriptor.Descriptor(
  name='RepeatedMACAddress',
  full_name='fmp.RepeatedMACAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='fmp.RepeatedMACAddress.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=105,
)

_REPEATEDMACADDRESS.fields_by_name['values'].message_type = _MACADDRESS
DESCRIPTOR.message_types_by_name['MACAddress'] = _MACADDRESS
DESCRIPTOR.message_types_by_name['RepeatedMACAddress'] = _REPEATEDMACADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MACAddress = _reflection.GeneratedProtocolMessageType('MACAddress', (_message.Message,), {
  'DESCRIPTOR' : _MACADDRESS,
  '__module__' : 'fmp.yang_pb2'
  # @@protoc_insertion_point(class_scope:fmp.MACAddress)
  })
_sym_db.RegisterMessage(MACAddress)

RepeatedMACAddress = _reflection.GeneratedProtocolMessageType('RepeatedMACAddress', (_message.Message,), {
  'DESCRIPTOR' : _REPEATEDMACADDRESS,
  '__module__' : 'fmp.yang_pb2'
  # @@protoc_insertion_point(class_scope:fmp.RepeatedMACAddress)
  })
_sym_db.RegisterMessage(RepeatedMACAddress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
