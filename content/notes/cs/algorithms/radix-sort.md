---
title: "Radix Sort"
tags:
  - cs/algorithms
  - cs/sorting
created: 2022-10-24
type: note
---
# Radix Sort
It is a non-comparison sorting method which only works on **binary** or **integer** data.

It takes $O(nb)$ time complexity, where:
- $n$ is the number of items.
- $b$ is the number of bits.
- best, worse and average case.

It is **very fast**.

It works by using a binary bucked sort for each binary digit:

1. Sort by the least significant bit.
2. Split input into 2 sets (bucket) based on the bit, those that have a 0 and those that have a 1 (ordering of data must be maintained).
3. Proceed to the next significant bit and repeat until we run out.

![[Screenshot 2022-10-24 at 17.13.50.png|400]]


> [!nav]
> [[cs-hub|Computer Science]]
