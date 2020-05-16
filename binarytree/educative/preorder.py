from .bst_recursive import BinarySearchTree


def preOrderTraversal(node):

    if node is not None:
        print(node.val)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)