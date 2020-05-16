class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, data):
        # create a temp node for data
        temp_node = Node(data)

        # let your temp node point to data which
        # head node is pointing to
        temp_node.next = self.head

        self.head = temp_node

        return self.head

    def insert_at_end(self, data):
        # create a temp node
        temp_node = Node(data)

        if self.is_empty():
            self.insert_at_head(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = temp_node
            return self.head

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(f"{temp.data} => ", end="")
            temp = temp.next
        print(" end")


if __name__ == "__main__":
    li = LinkedList()
    li.insert_at_head(5)
    li.insert_at_head(7)
    li.insert_at_end(10)
    li.print_list()
