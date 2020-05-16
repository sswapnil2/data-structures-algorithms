# deepest node in tree using level order traversal

from data import get_sample_data


def without_recursion(root):
    deepest_node = None
    if not root:
        return None

    queue = []
    queue.append(root)
    while queue:
        deepest_node = queue.pop(0)
        if deepest_node.left:
            queue.append(deepest_node.left)
        if deepest_node.right:
            queue.append(deepest_node.right)

    return deepest_node.data


if __name__ == "__main__":
    print(without_recursion(get_sample_data()))
