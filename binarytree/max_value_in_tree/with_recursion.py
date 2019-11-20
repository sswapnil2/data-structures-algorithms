# find the max value in left subtree and find the max_value in right subtree
# then compare it with root node
# return the largest

from data import get_sample_data


def find_max(root):
    if root:
        return max(root.data, find_max(root.left), find_max(root.right))
    return 0


if __name__ == "__main__":
    root = get_sample_data()
    print(find_max(root))
