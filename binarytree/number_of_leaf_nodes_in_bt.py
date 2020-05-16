# find number of leaf nodes in binary tree
# leaf is node whose both left and right child is null
# count using level order traversal


def count_leaf_nodes(root):
    if not root:
        return None

    queue = []
    queue.append(root)
    while root:
        root = queue.pop(0)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        if not root.left and not root.right:
            count += 1
