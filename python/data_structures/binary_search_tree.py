from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    A super class of the Binary Tree that add values and searches for the existence of a value
    """
    # Either do this, or get rid of it because init is being conducted in sub class binarytree
    def __init__(self):
        # initialization here
        super().__init__()

    def add(self, value):

        node = Node(value)
        # covers edge case if root is None
        if self.root is None:
            self.root = node
            return

        def walk(node, node_to_add):
            """
                10 want to add 5
                5 is less than 10 so need to add left

            """

            if node is None:
                return

            if node_to_add.value < node.value:
                if node.left is None:
                    node.left = node_to_add
                    return
                else:
                    walk(node.left, node_to_add)
                    return
            elif node_to_add.value >= node.value: # here is node_to_add > node.value
                if node.right is None:
                    node.right = node_to_add
                    return
                else:
                    walk(node.right, node_to_add)
                    return
        
        walk(self.root, node)

    def contains(self, value):
        def search(node):
            if node is None:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return search(node.left)
            else:
                return search(node.right)

        return search(self.root)