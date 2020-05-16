from node import Node
class LinkList:

    def __init__(self):
        self.head = None 
    
    def get_head(self):
        return self.head
    
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, dt):

        temp_node = Node(dt)

        if self.is_empty():
            self.head = temp_node
        else:
            temp_node.next = self.head
            self.head = temp_node

        return self.head
    

    def insert_at_tail(self, dt):

        temp_node = Node(dt)

        if self.get_head() is None:
            self.head = temp_node
            return self.head
        
        head = self.get_head()

        while head.next is not None:
            head = head.next
        
        head.next = temp_node

        return self.head

    def length(self):
        length = 0

        head = self.get_head()

        if head is None:
            return length

        while head is not None:
            length += 1
            head = head.next

        return length


    def print_list(self):

        if (self.is_empty()):
            print("List is empty")
            return 

        temp = self.head

        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print(temp.data, end=" -> None")

        return True

    
    # delete head node
    def delete_at_head(self):
        if (self.is_empty()):
            print("List is empty")
            return
        
        head = self.get_head()
        self.head = head.next

        return 


    def delete(self, value):
        deleted = False
        if (self.is_empty()):
            print("Cannot delete as list is empty")
            return deleted

        current_node = self.get_head()

        if current_node.data is value:
            self.delete_at_head()
            deleted = True
            return deleted
        
        previous_node = None
        while current_node is not None:
            if value is current_node.data:
                previous_node.next = current_node.next
                deleted = True
                break             
            previous_node = current_node
            current_node = current_node.next

        return deleted


        