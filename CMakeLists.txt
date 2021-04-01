cmake_minimum_required(VERSION 3.15)
#set(ENV{LSAN_OPTIONS} "verbosity=1:log_threads=1")
set(TargetName DataStores)
set(CPPUTILITIES_MAJOR_VERSION 1)
set(CPPUTILITIES_MINOR_VERSION 1)
set(CPPUTILITIES_PATCH_VERSION 1)
set(PACKAGE_VERSION ${CPPUTILITIES_MAJOR_VERSION}.${CPPUTILITIES_MINOR_VERSION}.${CPPUTILITIES_PATCH_VERSION})

project(
  ${TargetName}
  VERSION ${PACKAGE_VERSION}
  DESCRIPTION "C++17 header only utilities library"
  HOMEPAGE_URL "https://github.com/snhobbs/${TargetName}"
  LANGUAGES CXX
)

add_library(${TargetName} INTERFACE)
add_library(${TargetName}::${TargetName} ALIAS ${TargetName})

target_include_directories(
  ${TargetName} INTERFACE
  "${CMAKE_CURRENT_SOURCE_DIR}/include"
)

set(PACKAGE_NAME ${TargetName})
string(TOUPPER ${PACKAGE_NAME} PACKAGE_NAME_UPPER)

#-----------------------------------------------------------------------------

