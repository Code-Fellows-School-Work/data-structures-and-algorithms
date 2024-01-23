# class Node, Class Stack, __init__, push, pop, is_empty methods created in class with Adam as the instructor

from data_structures.invalid_operation_error import InvalidOperationError

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
        """
        Method to create a new node, point the new node to the top and reassigns self.top in the stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Method to remove top node from stack and raises an error if stack is empty
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        
        pop_value = self.top.value

        # move the pointer which "removes" the node from the Stack
        self.top = self.top.next

        return pop_value
    
    def is_empty(self):

        return self.top is None
           
    def peek(self):
        """Peek will only review the node at the top of the stack.
        Method checks the value of the node on the top and returns that value
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        
        return self.top.value
        # else:
        #     value = self.top.value
        #     return value
        
    