# Inroder  traversal with recursion
#       D
#     /  \
#   l     R
# In InOrder first traverse L then D then R

from data import get_sample_data


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


if __name__ == "__main__":
    root = get_sample_data()
    inorder(root)
