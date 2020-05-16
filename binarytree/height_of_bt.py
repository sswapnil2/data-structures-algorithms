from data import get_sample_data

# height of binary tree can be find with dfs or preorder traversal


def with_recursion(root):
    if not root:
        return 0

    left_height = with_recursion(root.left)
    right_height = with_recursion(root.right)
    return left_height + 1 if left_height > right_height else right_height + 1


# using level order traversal or bfs
def without_recursion(root):
    queue = []
    height = 0
    if not root:
        return 0
    queue.append(root)
    queue.append(None)  # end marker for first level
    while queue:
        root = queue.pop(0)
        if not root:
            if queue:
                queue.append(None)
            height += 1
        else:
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

    return height


if __name__ == "__main__":
    print(with_recursion(get_sample_data()))
    print(without_recursion(get_sample_data()))

