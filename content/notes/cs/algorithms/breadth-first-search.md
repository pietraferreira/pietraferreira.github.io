---
title: "Breadth-First Search"
tags:
  - cs/algorithms
created: 2022-11-07
type: note
---
It explores the graph differently from [[depth-first-search|depth-first search]].

It considers the **neighbouring** nodes first:
- All the neighbours at the start node are expanded first.
- Then the neighbours of the neighbours.
- Until the goal state is found.

It is a very expensive search since all the partial paths being considered must be stored.

It will eventually find a path to the goal but it may not be the best path.

It is similar to the [[exhaustive-search]] but it stops when the goal node is reached.

![[Screenshot 2022-11-07 at 11.32.54.png|400]]

## Visualisation
Breadth-First Search: [https://www.cs.usfca.edu/~galles/visualization/BFS.html](https://www.cs.usfca.edu/~galles/visualization/BFS.html)


> [!nav]
> [[cs-hub|Computer Science]]
