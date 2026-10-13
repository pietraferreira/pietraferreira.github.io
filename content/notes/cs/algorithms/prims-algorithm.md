---
title: "Prim's Algorithm"
tags:
  - work/engineer-training
  - cs/algorithms
created: 2022-06-06
type: note
---
# Prim's Algorithm
---
It is a [[minimum-spanning-tree]] algorithm.

It scales well, fast with dense [[graphs]].

It has a [[compiler-optimisation#Performance|performance]] of $O_{E\ log\ N}$ with [[binary-heap]] and $O_{E\ +\ log\ N}$ with Fibonacci heap.

It works like this:
1. Choose any node.
2. Choose nearest node that is not included in the spanning subtree formed so far.
3. Repeat step 2 until all nodes are included in the subtree.

![[prims.png]]

## Pseudo-Code
```
Algorithm 4. PrimsMST(G=(V,E))  
Input: G- a weighted graph (V- vertices, E- Edges)  
1) Let x be a random node from V  
2) Let Vnew = {x}  
3) Let Enew = {}  
4) While Vnew  V  
5) Choose an edge (u,v) with minimal weight,  
such that u  Vnew and v  Vnew  
6) Vnew = Vnew  {v}  
7) Enew = Enew  {(u,v)}  
8) Wend  
Output: Gnew = (Vnew,Enew)
```

## Example
![[Screenshot 2022-11-07 at 11.48.43.png|650]]

## See also
- [[minimum-spanning-tree]]
- [[trees]]
- [[graphs]]
- [[big-o-notation]]
- [[kruskals-algorithm|Kruskal's]]


> [!nav]
> [[cs-hub|Computer Science]]
