# class Node, Class Stack, __init__, push, pop, is_empty methods created in class with Adam as the instructor
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    """
    Pushes a new value onto the top of the stack.
    Removes the top value from the stack and returns it.
    """

    def __init__(self):
        self.top = None


    def push(self, value):
        # creates a new node
        new_node = Node(value)
        # point the new node to the current top
        new_node.next = self.top
        # reassign the self.top in the stack
        self.top = new_node

    def pop(self):
        # popping from an empty list
        # TODO: change this to raise an error
        if self.top is None:
            return None
            # raise InvalidOperationError("Method not allowed on an empty collection")
        
        # get the return value
        pop_value = self.top.value

        # move the pointer which "removes" the node from the Stack
        self.top = self.top.next

        return pop_value
    
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return "Method not allowed on empty collection"
    
    def peek(self):
        """Peek will only review the node at the top of the stack.
        Method checks the value of the node on the top and returns that value
        """
        value = self.top.value
        return value
        