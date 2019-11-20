# do traversal in whichever order you want and rathar than printing value
# calculate max
from data import get_sample_data


def process(root):
    stack = []
    max_val = -1
    while root:
        if max_val < root.data:
            max_val = root.data
        stack.append(root)
        root = root.left

        if not stack:
            break
        root = stack.pop(-1)
        root = root.right

    return max_val


if __name__ == "__main__":
    print(process(get_sample_data()))

