# - Config file for the DataStores package
# It defines the following variables
#  DATASTORES_INCLUDE_DIRS - include directories for DataStores
#  DATASTORES_LIBRARIES    - libraries to link against
#  DATASTORES_EXECUTABLE   - the bar executable

# Compute paths
get_filename_component("DATASTORES_CMAKE_DIR" "${CMAKE_CURRENT_LIST_FILE}" PATH)
set("DATASTORES_INCLUDE_DIRS" "/home/simon/software/DataStores;/home/simon/software/DataStores")
