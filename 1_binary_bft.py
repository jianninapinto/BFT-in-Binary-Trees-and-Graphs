# import the deque class from the collections module
from collections import deque

# define a node class representing a node in a binary tree
class node:
    def __init__(self, value):
        self.value = value
        self.left = None # left child
        self.right = None # right child

# define a function that takes a root node and performs bft
def traverse(root: node):
    queue = deque() # create an empty queue by instantiating deque
    values = [] # create an empty list to store visited node's values in traversal order
    # your BFT code here
    # Enqueue: queue.append(value)
    queue.append(root) # enqueue the root node into the queue
    # while there are nodes in the queue
    while queue:
        # Dequeue: queue.popleft(value)
        # dequeue a node from the front of the queue to get the next node to be visited
        current = queue.popleft()
        # append the current node's value to the values list to record nodes in traversal order
        values.append(current.value)

        # check if current node has a left child
        if current.left is not None:
            # enqueue left child into the queue
            queue.append(current.left)
        # check if current node has a right child
        if current.right is not None:
            # enqueue right child into the queue
            queue.append(current.right)

    # Once queue is empty, return the values list
    return values

# Implement a breadth-first traversal (BFT) for a binary tree. 
# Inputs: 
#   root: node (root of the binary tree)

# Output: list of values in the order of a breadth-first traversal 


# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 6, 3, 9