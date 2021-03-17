# Data Stores 

## Purpose
- Allow for data to be indexed and serialized by offset for use by offset protocols like Modbus.

## Goals
- Treats a struct as a single blob allowing for reading and writing serialized 
  sections using an offset
- Allows reading and writing of the sections of the struct in an normal manner.
- Memory and code size efficient
- No dynamic memory allocation
- Minimal copying
- Minimal use of dependancies

## Requirements
- Allows a controller to check the bounds of the datastore
  - This is used to prevent partial writes or reads
- Alligned data accesses

## Description
- Code generator for serializing a deserializing a struct description.
Useful for writing to/from bits and for serializing to Modbus registers.
- Currently supports:
  - Python
  - C++
  - WindLDR (IDEC PLCs)

## Enhancements
- Tool should extend a basic flatbuffers script which allows for fixed size
- Add padding when subsequent entries are not seperated by a multiple of 4 bytes
