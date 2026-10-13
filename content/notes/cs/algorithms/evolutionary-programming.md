---
title: "Evolutionary Programming"
tags:
  - cs/algorithms
created: 2023-02-03
type: note
---
---
Similar to [[intro-gen-algorithms|Genetic Algorithms]].

The emphasis here is on **mutation** and there is **no crossover**.

Every individual mutates, doubling the population.

The selection/survival operator tends to be **Tournament Selection**.

## Tournament Selection
---
Each member of the population is compared with a fixed number of other individuals. For each comparison, the individual is awarded a point if it's fitness is better than the opponent. The population is then reduced back to its original size by retaining those with the highest score.

### Pseudo-Code
---
```
Input: Population size, number of generations  
and Fitness Function  
1) Create the initial population  
2) For i = 1 to number of generations  
3) Mutate the population  
4) Apply Tournament Selection  
5) End For  
Output: Return the best individual
```
# Genetic Programming
---
It extends Genetic Algorithms.

We evolve computer programs by Natural Selection.

**Symbolic Regression** is a type of Genetic Programming, which represents a mathematical expression as a tree structure.

![[Screenshot 2023-02-03 at 14.13.27.png]]


> [!nav]
> [[cs-hub|Computer Science]]
