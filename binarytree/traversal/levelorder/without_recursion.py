# breadth first search called in graph algorithms

from data import get_sample_data


def level_order_traversal(root):
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        print(root.data)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


if __name__ == "__main__":
    level_order_traversal(get_sample_data())
