import random

class Node:
    def __init__(self, val):
        self.right_child = None
        self.left_child = None
        self.val = val
        self.parent = None

    def insert(self, val):
        if val < self.val:
            if self.left_child is not None:
                self.left_child.insert(val)
            else:
                self.left_child = Node(val)
                return
        else:
            if self.right_child is not None:
                self.right_child.insert(val)
            else:
                self.right_child = Node(val)

    def search(self, val):
        if not self:
            return False
        if self.val == val:
            return True

        elif  self.val > val:
            if self.right_child:
                return self.right_child.search(val)
            return False
        else:
            if self.left_child:
                return self.left_child.search(val)
            return False

    
    def delete(self, val):
        
        # when value is less than val
        if  val < self.val:
            if self.left_child:
                # found left child
                self.left_child = self.left_child.delete(val)
            else:
                # not found left child reached end
                return None

        elif val > self.val:
            # found right child
            if self.right_child:
                # found right child
                self.right_child = self.right_child.delete(val)
            else:
                # not found right child
                return None
        
        else:

            # case 1 when leaf node
            if self.left_child is None and self.right_child is None:
                self = None
                return None
            
            # case 2 when only left child
            elif self.left_child is None:
                temp = self.right_child
                self = None
                return temp

            elif self.right_child is None:
                temp = self.left_child
                self = None
                return temp
            

            # in case when node has left and right child
            else:
                current = self.right_child
                while(current.left_child):
                    # go til last smallest left node
                    current = current.left_child
                
                self.val = current.val
                self.right_child = self.right_child.delete(self.val)
        return self

        



        # when current value is greater than val

        # when val is found


        # while current:
        #     # insert into left substree
        #     if val < current.val:
        #         # case where left subchild is not present
        #         if self.left_child is None:
        #             self.left_child = Node(val)
        #             self.left_child.parent = current
        #             current = None
        #         else:
        #             # traverse the left subtree tree
        #             current = self.left_child
        #     # insert into right subtree
        #     else:
        #         if self.right_child is None:
        #             self.right_child = Node(val)
        #             self.right_child.parent = current
        #             current = None
        #         else:
        #             # traverse right subtree
        #             current = self.right_child





class BinarySearchTree:

    def __init__(self, val):
        self.root = Node(val)


    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True


    def search(self, val):
        if self.root:
            return self.root.search(val)
        return False

    def delete(self, val):
        if self.root is not None:
            return self.root.delete(val)



def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.right_child is None and node.left_child is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right_child is None:
        lines, n, p, x = _display_aux(node.left_child)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left_child is None:
        lines, n, p, x = _display_aux(node.right_child)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left_child)
    right, m, q, y = _display_aux(node.right_child)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    BST.insert(ele)
# We have hidden the code for this function but it is available for use!
display(BST.root)
print('\n')
print("Result: ", BST.search(50))  # Will print True since 50 is the root
print("Result: ", BST.search(11))

