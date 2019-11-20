# size of binary tree represents number of elements in binary tree

from data import get_sample_data


def size_of_bt_recursivly(root):
    if not root:
        return 0
    return size_of_bt_recursivly(root.left) + 1 + size_of_bt_recursivly(root.right)


def size_of_bt_without_recursion(root):
    if not root:
        return 0
    q = []
    count = 0
    q.append(root)
    while q:
        temp = q.pop(0)
        count += 1
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return count


if __name__ == "__main__":
    print(size_of_bt_recursivly(get_sample_data()))
    print(size_of_bt_without_recursion(get_sample_data()))
