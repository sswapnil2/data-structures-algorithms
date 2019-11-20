from data import get_sample_data
from data import Node


def insertion_with_recursion(root, number):

    if not root:
        return
    if root.left:
        insertion_with_recursion(root.left, number)
    else:
        root.left = Node(number)

    if root.right:
        insertion_with_recursion(root.right, number)
    else:
        root.right = Node(number)


def insertion_without_recursion(root, number):

    if not root:
        return 
    
    q = []
    q.append(root)
    while root:
        root = q.pop(0)
        if root.left:
            q.append(root.left)
        else:
            root.left = Node(number)
        if root.right:
            q.append(root.right)
        else:
            root.right = Node(number)


if name == "__main__":
    insertion_with_recursion(get_sample_data(), 5)
    insertion_without_recursion(get_sample_data(), 5)
