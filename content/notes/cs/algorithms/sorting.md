---
title: "Sorting"
tags:
  - cs/algorithms
created: 2022-06-05
type: note
---
# Sorting
---
The sorting problem is a mapping from $x$ to $y$, where:
- $x$ and $y$ are both **n** length real vectors (lists and/or arrays).
- $y$ is a permutation of $x$ (different ordering).
- $y_i < y_{i+1}$ for all $i = 0, ..., n-1$.

It is the problem or reordering items of an array in a certain order.

## Sorting methods
- [[bubble-sort]]
- [[quicksort]]
- [[radix-sort]]
- [[shell-sort]]
- [[heapsort]]
- [[bucket-sort]]
- [[selection-sort]]

## Stability
A **stable** sort guarantee to preserve the ordering from a first sort, where the second sort finds the records to be equal.

An **unstable** sort does not make this guarantee. Unstable methods can all be made stable.

### Examples
- Stable methods:
    - Merge sort and variants.
    - Variants of [[bubble-sort]].
    - Insertion sort and variants.
    - Variants on [[bucket-sort]].
        - Counting sort and variants.
    - Timsort (merge/insertion variant, Python).

## Comparison of Sorting Algorithms
![[Screenshot 2022-10-24 at 17.11.12.png]]


> [!nav]
> [[cs-hub|Computer Science]]
