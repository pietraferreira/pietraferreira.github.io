---
title: "Lists"
tags:
  - work/engineer-training
  - cs/data-structures
created: 2022-06-05
type: note
---
# Lists
---
A **list** is a sequence of zero or more data items, with the total number of items being the **length** of the list.

It can grow and shrink on demand and items can be accessed, inserted or deleted at any position.

![[lists.png]]

---
## Types of Lists
- [[arrays]]
- [[linked-list]]
- [[stack]]
- [[queue]]
- [[hash-tables]]

## Lists in C
```c
struct elem {
  struct elem *next;
  int val;
};
```

```c
struct elem
  struct elem *next;
  struct elem *head;
  int val;
};
```

```c
struct elem *head = NULL;
struct elem *tail = NULL;
```
## Applications
- Often used to implement other data structures e.g. [[queue]]s and [[stack]]s  
- Used for mathematical vectors and matrices


> [!nav]
> [[cs-hub|Computer Science]]
