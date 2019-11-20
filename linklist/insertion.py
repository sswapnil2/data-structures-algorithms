class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert(head: ListNode, value: int, position: int = 1) -> ListNode:
    """
        given the head node and position to 
        insert value into insert new value
    """
    # check if head node is none
    if head is None or position == 1:  # if head is not present or position ==1
        # enter into first position
        tempNode = ListNode(value)  # create temp Node
        tempNode.next = head  # set the node next value to head
        head = tempNode  # set the head refeerence to node
    else:
        p = head  # set p to head node
        k = 1  # set counter to 1
        q = p  # set temp variable q to value p
        while p is not None and k < position:
            k += 1  # increment the counter
            q = p  # set the previous value to q so it can be used as refernce laster
            p = p.next  # increment head pointer

        tempNode = ListNode(value)  # create temp node
        tempNode.next = (
            p
        )  # first set the value of p as next of temp to add whole connection
        q.next = tempNode  # then set prev pointer next to tempNode to add node

    return head


if __name__ == "__main__":
    head = ListNode(2)

    head = insert(head, 70, 1)

    head = insert(head, 80, 100)
    head = insert(head, 5, 2)

    while head is not None:
        print(head.value, end=" => ")
        head = head.next
