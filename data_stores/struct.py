import math
from enum import Enum


class DataType(Enum):
    uint8_t = 0
    int8_t = 1
    uint16_t = 2
    int16_t = 3
    uint32_t = 4
    int32_t = 5
    uint64_t = 6
    int64_t = 7
    kString = 8


class StorageType:
    uint8_t = DataType.uint8_t
    uint16_t = DataType.uint16_t
    uint32_t = DataType.uint32_t
    uint64_t = DataType.uint64_t


def GetDataTypeCType(dtype):
    if dtype == DataType.kString:
        return DataType.uint8_t.name
    else:
        return dtype.name


def GetDataTypeSize(dtype):
    if dtype in [DataType.uint8_t, DataType.int8_t, DataType.kString]:
        return 1
    elif dtype in [DataType.uint16_t, DataType.int16_t]:
        return 2
    elif dtype in [DataType.uint32_t, DataType.int32_t]:
        return 4
    if dtype in [DataType.uint64_t, DataType.int64_t]:
        return 8


class StructEntry:
    def __init__(self, name, dtype, base_length):
        self.name = name
        self.dtype = dtype
        self.base_length = base_length
        self._storage_type = None

        assert(type(self.name) is str)
        assert(type(self.dtype) is DataType)
        assert(self.base_length >= 1)

    @property
    def storage_type(self):
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        assert(type(storage_type) is DataType)
        self._storage_type = storage_type

    ''' Rounded up length to be integer multiple of storage type '''
    @property
    def length(self):
        return self.base_length + (GetDataTypeSize(self.dtype) * self.base_length) % GetDataTypeSize(self.storage_type)

    @property
    def storage_length(self):
        return int(math.ceil(float(GetDataTypeSize(self.dtype) * self.length) / GetDataTypeSize(self.storage_type)))

    @property
    def dtype_ctype(self):
        return GetDataTypeCType(self.dtype)


class Struct:
    def __init__(self, name, entries, storage_type=StorageType.uint8_t):
        self.name = name
        self.entries = entries
        for entry in self.entries:
            entry.storage_type = storage_type
