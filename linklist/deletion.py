from insertion import insert


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete(head: ListNode, position: int = 1) -> ListNode:
    """
        function takes head value and position to delete the node and returns 
        the head of the Link list
    """
    if position == 1:
        temp = head
        head = temp.next
        del temp
        return head

    k = 1  # position counter
    p = head
    q = p
    while p.next is not None and k < position:
        q = p
        p = p.next

    q.next = p.next
    return head


def print_dunction(head):
    while head is not None:
        print(head.value, end="\n" if head.next is None else " => ")
        head = head.next


if __name__ == "__main__":

    head = ListNode(5)
    head = insert(head, 10, 2)
    head = insert(head, 15, 3)
    head = insert(head, 20, 4)

    print_dunction(head)
    # deleting values
    print("deleting value at position: ", 1)
    head = delete(head, position=1)
    print_dunction(head)
    print("deleting value at position: ", 100)

    head = delete(head, position=100)
    print_dunction(head)
    print("deleting value a position: ", 2)
    head = delete(head, position=1)

    print_dunction(head)
