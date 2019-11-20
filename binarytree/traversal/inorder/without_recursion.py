# preorder traversal without recursion
# while doing preorder without recursion first we process the current node
# we use stack to keep track of current node
# first we process left subtree and then we process right subtree

from data import get_sample_data


def preorder_without_recursion(root):
    stack = []
    while True:
        while root:
            # process the current node
            stack.append(root)
            # if the left subtree exists push it to the stack
            root = root.left

        if not stack:  # if stack is empty
            break

        root = stack.pop(-1)
        print(root.data)

        # indicates the completion of left subtree then move to right subtree
        root = root.right


if __name__ == "__main__":
    preorder_without_recursion(get_sample_data())

