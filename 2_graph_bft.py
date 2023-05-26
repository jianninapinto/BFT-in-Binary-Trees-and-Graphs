# import the deque class from the collections module
from collections import deque

# define a function that takes a graph in the form of an adjacency list and root node to perform bft
def traverse(graph, root):
    # create an empty queue by instantiating the deque class
    queue = deque()
    # add starting node to the queue
    queue.append(root)
    # create an empty list to store the visited node's values in traversal order
    values = []
    # create a set to mark nodes as visited
    visited = set()
    # add root node to the visited set
    visited.add(root)

    # while queue is not empty
    while queue:
        # dequeue a vertex or node from the front of the queue
        current = queue.popleft()
        # append the current node's value to the values list
        values.append(current)

        # for each neighbor of the current node in the graph
        for neighbor in graph[current]:
            # if neighbor hasn't been visited yet
            if neighbor not in visited:
                # first append neighbor to the queue
                queue.append(neighbor)
                # mark neighbor as visited
                visited.add(neighbor)
    
    # Once the queue is empty, return the node's values
    return values

# Implement a breadth-first traversal (BFT) for a graph. 
# Inputs: 
#   graph: dict (adjacency list representation)
#   root: int (starting point for the traverse)

# Output: list of values in the order of a breadth-first traversal 

# Representing a graph as a Python dictionary provides a nice simplified version of an adjacency list implementation. The keys of the dictionary are vertices, and the key-value pairs in the dictionary map each vertex to a list of integers representing its neighbors.

# Test cases
# We'll be using this simple undirected graph to test our BFT:
# 5 -- 3
# | \
# |  2
# | / \
# 1    4
graph = {1: [2, 5], 2: [1, 4, 5], 3: [5], 4: [2], 5: [1, 2, 3]}
print(traverse(graph, 1)) # [1, 2, 5, 4, 3]
print(traverse(graph, 4)) # [4, 2, 1, 5, 3]
print(traverse(graph, 5)) # [5, 1, 2, 3, 4]