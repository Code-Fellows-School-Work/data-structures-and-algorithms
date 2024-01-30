class BinaryTree:
    """
    A class representing a Binary Tree data structure
    """
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        """
        Traverse the binary tree
        """
        """
             a
          b      c
        d  e    f  g
        [root node result: "a",     left node result: "b", "d", "e",    right node result: "c", "f", "g"]
        So looks like ["a"] + ["b", "d", "e"] + ["c", "f", "g"]
        """
        def walk(node):
            """
            Begins the walk at the root node
            """
            # need to add base case for recursive function because what if Node is none?
            if node is None:
                return []
            
            my_result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return my_result + left_result + right_result
        
        return walk(self.root)
    
    def in_order(self):
        # need to modify this docstring
        """
        ["d", "b", "e", "a", "f", "c", "g"]
        [root node result: "a",     left node result: "b", "d", "e",    right node result: "c", "f", "g"]
        So looks like ["a"] + ["b", "d", "e"] + ["c", "f", "g"]
        """
        def walk(node):
            """
            Begins the walk at the root node
            """
            # need to add base case for recursive function because what if Node is none?
            if node is None:
                return []
            
            my_result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return left_result + my_result + right_result
        
        return walk(self.root)
    
    def post_order(self):
        # need to modify this docstring
        """
        left --> root --> right
        [root node result: "a",     left node result: "b", "d", "e",    right node result: "c", "f", "g"]
        So looks like ["a"] + ["b", "d", "e"] + ["c", "f", "g"]
        """
        def walk(node):
            """
            Begins the walk at the root node
            """
            # need to add base case for recursive function because what if Node is none?
            if node is None:
                return []
            
            my_result = [node.value]
            left_result = walk(node.left)
            right_result = walk(node.right)

            return left_result + right_result + my_result 
        
        return walk(self.root)
    
    def contains(self):
        pass
    
    # Used ChatGPT to help write this code. I knew it had to be recusrive but could not figure out how to implement it
    def find_maximum_value(self):
        def find_max(node):

            if node is None:
                return 0
    
            left_max = find_max(node.left)
            right_max = find_max(node.right)
            return max(node.value, left_max, right_max)

        return find_max(self.root)
        
        

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


