# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: factorial.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='factorial.proto',
  package='factorial',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x66\x61\x63torial.proto\x12\tfactorial\"\x1e\n\x0c\x46\x61\x63torialReq\x12\x0e\n\x06number\x18\x01 \x01(\x05\"\x1e\n\x0c\x46\x61\x63torialRes\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32S\n\x10\x46\x61\x63torialService\x12?\n\tFactorial\x12\x17.factorial.FactorialReq\x1a\x17.factorial.FactorialRes\"\x00\x62\x06proto3'
)




_FACTORIALREQ = _descriptor.Descriptor(
  name='FactorialReq',
  full_name='factorial.FactorialReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='factorial.FactorialReq.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=30,
  serialized_end=60,
)


_FACTORIALRES = _descriptor.Descriptor(
  name='FactorialRes',
  full_name='factorial.FactorialRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='factorial.FactorialRes.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=62,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['FactorialReq'] = _FACTORIALREQ
DESCRIPTOR.message_types_by_name['FactorialRes'] = _FACTORIALRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FactorialReq = _reflection.GeneratedProtocolMessageType('FactorialReq', (_message.Message,), {
  'DESCRIPTOR' : _FACTORIALREQ,
  '__module__' : 'factorial_pb2'
  # @@protoc_insertion_point(class_scope:factorial.FactorialReq)
  })
_sym_db.RegisterMessage(FactorialReq)

FactorialRes = _reflection.GeneratedProtocolMessageType('FactorialRes', (_message.Message,), {
  'DESCRIPTOR' : _FACTORIALRES,
  '__module__' : 'factorial_pb2'
  # @@protoc_insertion_point(class_scope:factorial.FactorialRes)
  })
_sym_db.RegisterMessage(FactorialRes)



_FACTORIALSERVICE = _descriptor.ServiceDescriptor(
  name='FactorialService',
  full_name='factorial.FactorialService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=94,
  serialized_end=177,
  methods=[
  _descriptor.MethodDescriptor(
    name='Factorial',
    full_name='factorial.FactorialService.Factorial',
    index=0,
    containing_service=None,
    input_type=_FACTORIALREQ,
    output_type=_FACTORIALRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FACTORIALSERVICE)

DESCRIPTOR.services_by_name['FactorialService'] = _FACTORIALSERVICE

# @@protoc_insertion_point(module_scope)