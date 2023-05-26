
# Breadth-First Traversal (BFT) in Binary Trees and Graphs

This repository contains Python code that demonstrates the Breadth-First Traversal (BFT) algorithm for binary trees and graphs. The BFT algorithm allows you to visit all the nodes or vertices in a tree or graph in a breadth-first manner, exploring nodes at the same level before moving to the next level.

## Binary Tree BFT

The traverse(root) function implements the Breadth-First Traversal algorithm for binary trees. It takes a root node as input and returns a list of values in the order of a breadth-first traversal.

Example usage:

```
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head))  # [6, 3, 9]
```

## Graph BFT

The traverse(graph, root) function implements the Breadth-First Traversal algorithm for graphs. It takes a graph in the form of an adjacency list and a root node as input, and returns a list of values in the order of a breadth-first traversal.

Example usage:

```
graph = {1: [2, 5], 2: [1, 4, 5], 3: [5], 4: [2], 5: [1, 2, 3]}
print(traverse(graph, 1))  # [1, 2, 5, 4, 3]
print(traverse(graph, 4))  # [4, 2, 1, 5, 3]
print(traverse(graph, 5))  # [5, 1, 2, 3, 4]
```

In this implementation, the graph is represented as a dictionary where the keys represent the vertices, and the values are lists of integers representing the neighbors of each vertex.

## Credits

This code was created as part of a data structures and algorithms course at BloomTech.