# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nbook.proto\"&\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\t\"\x17\n\x05Reply\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x19\n\x07Request\x12\x0e\n\x06status\x18\x01 \x01(\x05\x32t\n\x04\x42ook\x12\x1e\n\tAddPerson\x12\x07.Person\x1a\x06.Reply\"\x00\x12!\n\x0cRemovePerson\x12\x07.Person\x1a\x06.Reply\"\x00\x12)\n\x10GetListOfPersons\x12\x08.Request\x1a\x07.Person\"\x00\x30\x01\x62\x06proto3')
)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='Person.number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=52,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Reply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=77,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Request.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'book_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), dict(
  DESCRIPTOR = _REPLY,
  __module__ = 'book_pb2'
  # @@protoc_insertion_point(class_scope:Reply)
  ))
_sym_db.RegisterMessage(Reply)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'book_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class BookStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.AddPerson = channel.unary_unary(
          '/Book/AddPerson',
          request_serializer=Person.SerializeToString,
          response_deserializer=Reply.FromString,
          )
      self.RemovePerson = channel.unary_unary(
          '/Book/RemovePerson',
          request_serializer=Person.SerializeToString,
          response_deserializer=Reply.FromString,
          )
      self.GetListOfPersons = channel.unary_stream(
          '/Book/GetListOfPersons',
          request_serializer=Request.SerializeToString,
          response_deserializer=Person.FromString,
          )


  class BookServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def AddPerson(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def RemovePerson(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetListOfPersons(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_BookServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AddPerson': grpc.unary_unary_rpc_method_handler(
            servicer.AddPerson,
            request_deserializer=Person.FromString,
            response_serializer=Reply.SerializeToString,
        ),
        'RemovePerson': grpc.unary_unary_rpc_method_handler(
            servicer.RemovePerson,
            request_deserializer=Person.FromString,
            response_serializer=Reply.SerializeToString,
        ),
        'GetListOfPersons': grpc.unary_stream_rpc_method_handler(
            servicer.GetListOfPersons,
            request_deserializer=Request.FromString,
            response_serializer=Person.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Book', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaBookServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def AddPerson(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def RemovePerson(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetListOfPersons(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaBookStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def AddPerson(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    AddPerson.future = None
    def RemovePerson(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    RemovePerson.future = None
    def GetListOfPersons(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_Book_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Book', 'AddPerson'): Person.FromString,
      ('Book', 'GetListOfPersons'): Request.FromString,
      ('Book', 'RemovePerson'): Person.FromString,
    }
    response_serializers = {
      ('Book', 'AddPerson'): Reply.SerializeToString,
      ('Book', 'GetListOfPersons'): Person.SerializeToString,
      ('Book', 'RemovePerson'): Reply.SerializeToString,
    }
    method_implementations = {
      ('Book', 'AddPerson'): face_utilities.unary_unary_inline(servicer.AddPerson),
      ('Book', 'GetListOfPersons'): face_utilities.unary_stream_inline(servicer.GetListOfPersons),
      ('Book', 'RemovePerson'): face_utilities.unary_unary_inline(servicer.RemovePerson),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Book_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Book', 'AddPerson'): Person.SerializeToString,
      ('Book', 'GetListOfPersons'): Request.SerializeToString,
      ('Book', 'RemovePerson'): Person.SerializeToString,
    }
    response_deserializers = {
      ('Book', 'AddPerson'): Reply.FromString,
      ('Book', 'GetListOfPersons'): Person.FromString,
      ('Book', 'RemovePerson'): Reply.FromString,
    }
    cardinalities = {
      'AddPerson': cardinality.Cardinality.UNARY_UNARY,
      'GetListOfPersons': cardinality.Cardinality.UNARY_STREAM,
      'RemovePerson': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Book', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
