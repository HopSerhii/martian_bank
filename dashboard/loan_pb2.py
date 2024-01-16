
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loan.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nloan.proto\"\xda\x01\n\x0bLoanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x03 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x04 \x01(\t\x12\x14\n\x0cgovt_id_type\x18\x05 \x01(\t\x12\x16\n\x0egovt_id_number\x18\x06 \x01(\t\x12\x11\n\tloan_type\x18\x07 \x01(\t\x12\x13\n\x0bloan_amount\x18\x08 \x01(\x01\x12\x15\n\rinterest_rate\x18\t \x01(\x01\x12\x13\n\x0btime_period\x18\n \x01(\t\"1\n\x0cLoanResponse\x12\x10\n\x08\x61pproved\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"$\n\x13LoansHistoryRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\xf6\x01\n\x04Loan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x03 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x04 \x01(\t\x12\x14\n\x0cgovt_id_type\x18\x05 \x01(\t\x12\x16\n\x0egovt_id_number\x18\x06 \x01(\t\x12\x11\n\tloan_type\x18\x07 \x01(\t\x12\x13\n\x0bloan_amount\x18\x08 \x01(\x01\x12\x15\n\rinterest_rate\x18\t \x01(\x01\x12\x13\n\x0btime_period\x18\n \x01(\t\x12\x0e\n\x06status\x18\x0b \x01(\t\x12\x11\n\ttimestamp\x18\x0c \x01(\t\",\n\x14LoansHistoryResponse\x12\x14\n\x05loans\x18\x01 \x03(\x0b\x32\x05.Loan2\x7f\n\x0bLoanService\x12\x31\n\x12ProcessLoanRequest\x12\x0c.LoanRequest\x1a\r.LoanResponse\x12=\n\x0egetLoanHistory\x12\x14.LoansHistoryRequest\x1a\x15.LoansHistoryResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'loan_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOANREQUEST._serialized_start=15
  _LOANREQUEST._serialized_end=233
  _LOANRESPONSE._serialized_start=235
  _LOANRESPONSE._serialized_end=284
  _LOANSHISTORYREQUEST._serialized_start=286
  _LOANSHISTORYREQUEST._serialized_end=322
  _LOAN._serialized_start=325
  _LOAN._serialized_end=571
  _LOANSHISTORYRESPONSE._serialized_start=573
  _LOANSHISTORYRESPONSE._serialized_end=617
  _LOANSERVICE._serialized_start=619
  _LOANSERVICE._serialized_end=746
# @@protoc_insertion_point(module_scope)
