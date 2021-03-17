import copy
from jinja2 import Template, Environment, FileSystemLoader
import data_stores
from data_stores import Struct, StructEntry, make, DataType
import sys

entries = (
    data_stores.StructEntry('version', DataType.kString, 64),
    data_stores.StructEntry('firmware_version', DataType.kString, 64),
    data_stores.StructEntry('compile_date', DataType.kString, 64),
    data_stores.StructEntry('compile_time', DataType.kString, 64),
    data_stores.StructEntry('serial_number', DataType.kString, 40),
    data_stores.StructEntry('slave_address', DataType.uint16_t, 1),
    data_stores.StructEntry('clear_faults', DataType.uint32_t, 1),
    data_stores.StructEntry('start_data_read', DataType.uint32_t, 1),
)

if __name__ == "__main__":
    make(Struct(name="InfoStruct", entries=entries, storage_type=DataType.uint8_t), "Struct.h")
