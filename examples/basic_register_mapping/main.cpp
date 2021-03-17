#include "Struct.h"

int main(void) {
  InfoStruct s{};
  InfoStructWrapper wrapper{&s};
  return 0;
}
