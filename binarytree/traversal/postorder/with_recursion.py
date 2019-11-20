# in post order
# first process left subtree then process right subtree and process root node
from data import get_sample_data


def process_tree(root):
    if root:
        process_tree(root.left)
        process_tree(root.right)
        print(root.data)


if __name__ == "__main__":
    process_tree(get_sample_data())
