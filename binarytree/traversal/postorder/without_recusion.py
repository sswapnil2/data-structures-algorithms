# without recursion
from data import get_sample_data


def is_empty(s):
    return not s


def p(root):
    global stack
    while root:
        stack.append(root)
        root = root.left
    while root == None and not is_empty(stack):
        root = stack[-1]
        if root.right == None or root.right == previous:
            print(root.data)
            stack.pop(-1)
            previous = root
            root = None
        else:
            root = root.right
    return root


stack = []


def process_tree(root):
    r = p(root)
    while stack:
        r = p(r)


if __name__ == "__main__":
    process_tree(get_sample_data())
