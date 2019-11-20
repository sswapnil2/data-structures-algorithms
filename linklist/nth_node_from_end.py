class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def add_node(head: Node, data: int) -> Node:
    node = Node(data)
    if head is None:
        head = node
    else:
        node.next = head
        head = node
    return head


def print_list(head: Node) -> None:
    temp = head

    while temp is not None:
        print(temp.data, end="-->")
        temp = temp.next
    print()


from time import time


def timit(func):
    def inner(*args):
        start = time()
        value = func(*args)
        end = time()
        print((end - start) * 1000)
        return value

    return inner


# hashing approach
@timit
def nth_node_from_end(head: Node, position: int) -> int:
    temp = head
    # to get nth node we need length of list
    temp_dict = {}
    count = 0
    while temp is not None:
        temp_dict[count] = temp.data
        temp = temp.next
        count += 1

    if position - 1 > count:
        print("Position exceeds list")
        return 0

    print(count)
    return temp_dict[count - position]


# one scan efficient approach
# fast and slow pointer apporach
@timit
def one_scan_approach(head: Node, position: int) -> int:
    temp = head
    temp2 = head

    for _ in range(position):
        temp = temp.next

    while temp is not None:
        temp = temp.next
        temp2 = temp2.next

    return temp2.data


if __name__ == "__main__":
    head = None
    elements = [5, 6, 8, 7, 45, 45, 7, 69, 2, 8]
    for element in elements:
        head = add_node(head, element)

    print_list(head)
    print(nth_node_from_end(head, 4))
    print(one_scan_approach(head, 4))

