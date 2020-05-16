# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.

import math

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def minimum_level_sum(node):
    # case when leaf node
    # so the minimum sum is itself
    if node is None:
        return math.inf
    
    # if left and right child are both none
    if node.left is None and node.right is None:
        return math.inf
    
    # minimum of level
    if node.right is None:
        return min(node.val + node.left.val, minimum_level_sum(node.left))
    
    if node.left is None:
        return min(node.val + node.right.val, minimum_level_sum(node.right))
    
    _sum = node.val + node.left.val + node.right.val
    return min(_sum, minimum_level_sum(node.left), minimum_level_sum(node.right))

#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2


node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))