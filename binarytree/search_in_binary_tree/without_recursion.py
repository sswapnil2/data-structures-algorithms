# perform level order traversal while searching for element
from data import get_sample_data


def search_without_recursion(root, search_item):
    queue = []
    if not root:
        return False
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        if temp.data == search_item:
            return True
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    return False


print(search_without_recursion(get_sample_data(), 10))
