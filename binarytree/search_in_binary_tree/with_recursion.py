from data import get_sample_data


def search_with_recursion(root, search_item):
    if not root:
        return False

    if root.data == search_item:
        return True
    temp = search_with_recursion(root.left, search_item)
    if temp:
        return True
    else:
        return search_with_recursion(root.right, search_item)


print(search_with_recursion(get_sample_data(), 1))
