# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amazon_ups.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='amazon_ups.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x61mazon_ups.proto\"\x1f\n\x0c\x41InformWorld\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\"!\n\x0eUReceivedWorld\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\"\xb7\x01\n\nABookTruck\x12\x11\n\tpackageid\x18\x01 \x02(\x03\x12\x13\n\x0bwarehouseid\x18\x02 \x02(\x05\x12\x12\n\nwarehousex\x18\x03 \x02(\x05\x12\x12\n\nwarehousey\x18\x04 \x02(\x05\x12\x14\n\x0c\x64\x65stinationx\x18\x05 \x02(\x05\x12\x14\n\x0c\x64\x65stinationy\x18\x06 \x02(\x05\x12\r\n\x05upsid\x18\x07 \x01(\t\x12\x0e\n\x06seqnum\x18\x08 \x01(\x03\x12\x0e\n\x06\x64\x65tail\x18\t \x01(\t\"C\n\rUTruckArrived\x12\x11\n\tpackageid\x18\x01 \x02(\x03\x12\x0f\n\x07truckid\x18\x02 \x02(\x05\x12\x0e\n\x06seqnum\x18\x03 \x01(\x03\"2\n\rAStartDeliver\x12\x11\n\tpackageid\x18\x01 \x02(\x03\x12\x0e\n\x06seqnum\x18\x02 \x01(\x03\"/\n\nUDelivered\x12\x11\n\tpackageid\x18\x01 \x02(\x03\x12\x0e\n\x06seqnum\x18\x02 \x01(\x03\"`\n\x0f\x41UCommunication\x12\x1d\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\x0b.ABookTruck\x12 \n\x08\x64\x65livers\x18\x02 \x03(\x0b\x32\x0e.AStartDeliver\x12\x0c\n\x04\x61\x63ks\x18\x03 \x01(\x03\"`\n\x0fUACommunication\x12\x1f\n\x07\x61rrived\x18\x01 \x03(\x0b\x32\x0e.UTruckArrived\x12\x1e\n\tdelivered\x18\x02 \x03(\x0b\x32\x0b.UDelivered\x12\x0c\n\x04\x61\x63ks\x18\x03 \x01(\x03')
)




_AINFORMWORLD = _descriptor.Descriptor(
  name='AInformWorld',
  full_name='AInformWorld',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='AInformWorld.worldid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=51,
)


_URECEIVEDWORLD = _descriptor.Descriptor(
  name='UReceivedWorld',
  full_name='UReceivedWorld',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldid', full_name='UReceivedWorld.worldid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=86,
)


_ABOOKTRUCK = _descriptor.Descriptor(
  name='ABookTruck',
  full_name='ABookTruck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='ABookTruck.packageid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouseid', full_name='ABookTruck.warehouseid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehousex', full_name='ABookTruck.warehousex', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehousey', full_name='ABookTruck.warehousey', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destinationx', full_name='ABookTruck.destinationx', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destinationy', full_name='ABookTruck.destinationy', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upsid', full_name='ABookTruck.upsid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='ABookTruck.seqnum', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='ABookTruck.detail', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=272,
)


_UTRUCKARRIVED = _descriptor.Descriptor(
  name='UTruckArrived',
  full_name='UTruckArrived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UTruckArrived.packageid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truckid', full_name='UTruckArrived.truckid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UTruckArrived.seqnum', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=341,
)


_ASTARTDELIVER = _descriptor.Descriptor(
  name='AStartDeliver',
  full_name='AStartDeliver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='AStartDeliver.packageid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='AStartDeliver.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=393,
)


_UDELIVERED = _descriptor.Descriptor(
  name='UDelivered',
  full_name='UDelivered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageid', full_name='UDelivered.packageid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='UDelivered.seqnum', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=442,
)


_AUCOMMUNICATION = _descriptor.Descriptor(
  name='AUCommunication',
  full_name='AUCommunication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookings', full_name='AUCommunication.bookings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delivers', full_name='AUCommunication.delivers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acks', full_name='AUCommunication.acks', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=540,
)


_UACOMMUNICATION = _descriptor.Descriptor(
  name='UACommunication',
  full_name='UACommunication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arrived', full_name='UACommunication.arrived', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delivered', full_name='UACommunication.delivered', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acks', full_name='UACommunication.acks', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=638,
)

_AUCOMMUNICATION.fields_by_name['bookings'].message_type = _ABOOKTRUCK
_AUCOMMUNICATION.fields_by_name['delivers'].message_type = _ASTARTDELIVER
_UACOMMUNICATION.fields_by_name['arrived'].message_type = _UTRUCKARRIVED
_UACOMMUNICATION.fields_by_name['delivered'].message_type = _UDELIVERED
DESCRIPTOR.message_types_by_name['AInformWorld'] = _AINFORMWORLD
DESCRIPTOR.message_types_by_name['UReceivedWorld'] = _URECEIVEDWORLD
DESCRIPTOR.message_types_by_name['ABookTruck'] = _ABOOKTRUCK
DESCRIPTOR.message_types_by_name['UTruckArrived'] = _UTRUCKARRIVED
DESCRIPTOR.message_types_by_name['AStartDeliver'] = _ASTARTDELIVER
DESCRIPTOR.message_types_by_name['UDelivered'] = _UDELIVERED
DESCRIPTOR.message_types_by_name['AUCommunication'] = _AUCOMMUNICATION
DESCRIPTOR.message_types_by_name['UACommunication'] = _UACOMMUNICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AInformWorld = _reflection.GeneratedProtocolMessageType('AInformWorld', (_message.Message,), dict(
  DESCRIPTOR = _AINFORMWORLD,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AInformWorld)
  ))
_sym_db.RegisterMessage(AInformWorld)

UReceivedWorld = _reflection.GeneratedProtocolMessageType('UReceivedWorld', (_message.Message,), dict(
  DESCRIPTOR = _URECEIVEDWORLD,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UReceivedWorld)
  ))
_sym_db.RegisterMessage(UReceivedWorld)

ABookTruck = _reflection.GeneratedProtocolMessageType('ABookTruck', (_message.Message,), dict(
  DESCRIPTOR = _ABOOKTRUCK,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:ABookTruck)
  ))
_sym_db.RegisterMessage(ABookTruck)

UTruckArrived = _reflection.GeneratedProtocolMessageType('UTruckArrived', (_message.Message,), dict(
  DESCRIPTOR = _UTRUCKARRIVED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UTruckArrived)
  ))
_sym_db.RegisterMessage(UTruckArrived)

AStartDeliver = _reflection.GeneratedProtocolMessageType('AStartDeliver', (_message.Message,), dict(
  DESCRIPTOR = _ASTARTDELIVER,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AStartDeliver)
  ))
_sym_db.RegisterMessage(AStartDeliver)

UDelivered = _reflection.GeneratedProtocolMessageType('UDelivered', (_message.Message,), dict(
  DESCRIPTOR = _UDELIVERED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UDelivered)
  ))
_sym_db.RegisterMessage(UDelivered)

AUCommunication = _reflection.GeneratedProtocolMessageType('AUCommunication', (_message.Message,), dict(
  DESCRIPTOR = _AUCOMMUNICATION,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUCommunication)
  ))
_sym_db.RegisterMessage(AUCommunication)

UACommunication = _reflection.GeneratedProtocolMessageType('UACommunication', (_message.Message,), dict(
  DESCRIPTOR = _UACOMMUNICATION,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UACommunication)
  ))
_sym_db.RegisterMessage(UACommunication)


# @@protoc_insertion_point(module_scope)
