#pragma once
#include <cstdint>
namespace DataStores {
template<typename T>
struct StructEntry {
  const T identifier;
  const std::size_t offset;
  const std::size_t size;
};
}  //  namespace DataStores
