# pre order traversal with recursion
#       D
#     /  \
#   l     R
# In preorder first traverse D then L then R

from traversal.data import get_sample_data
from traversal.data import Node


def preorder_traversal_with_recursion(root):
    if root:
        print(root.data)
        preorder_traversal_with_recursion(root.left)
        preorder_traversal_with_recursion(root.right)


if __name__ == "__main__":
    preorder_traversal_with_recursion(get_sample_data())
