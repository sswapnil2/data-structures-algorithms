from data import get_sample_data


def print_level_order_reverse(root):
    q = []
    s = []
    q.append(root)
    while q:
        temp = q.pop(0)
        s.append(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    for i in list(reversed(s)):
        print(i)


if __name__ == "__main__":
    print_level_order_reverse(get_sample_data())
