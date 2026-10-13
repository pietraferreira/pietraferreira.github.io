---
title: "Ideas"
tags:
  - inbox
created: 2026-10-13
type: note
---

# Ideas

## 2026-10-13 11:25
`void` is **no type**, thus it can't be instantiated:

```cpp
void value; // won't work
```

We use it a lot for functions that do not return a value.

A **pointer** on a 64-bit system is 64-bits (8 bytes), an **integer** however is
4 bytes (32 bits), and a **char** is 1 byte (8 bits).

A 32 bit integer wouldn't fit in a 16 bit device - for this we can use **fixed-width** integers:

```cpp
#include <cstdint>
#include <iostream>

int main()
{
    std::int32_t x { 32767 }; // x is always a 32-bit int
    x = x + 1;
    std::cout << x << '\n';

    return 0;
}
```
