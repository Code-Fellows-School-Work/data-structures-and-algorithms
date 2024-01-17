# Used JB's class code to help write below code
class Node:
    """
    Class function to create a node in a linked list
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Class function to create instance of a linked list. 

    :param: first node in the linked list initialized to none

    :methods:
        includes: - checks if a value is present
        insert: - adds a new node with the given value as the head
        __str__: - string representation of the linked list
        append: - adds a new node with the given value as the tail
        insert_before: - adds a new node with a new value before the target value node
        insert_after: - adds a new node with a new value after the target value node
    """

    def __init__(self):
        self.head = None

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):

        result = []
        current = self.head

        string_representation = ""

        while current:
            string_representation += f"{{ {current.value} }} -> "
            current = current.next

        string_representation += "NULL"
        return string_representation
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, value):
        if self.head is None:
            return False
        
        if self.head.value == target:
            self.insert(value)
            return True
        
        current = self.head
        while current.next:
            if current.next.value == target:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

        return False
    
    def insert_after(self, target, value):
        new_node = Node(value)
        current = self.head

        while current:
            if current.value == target:
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

        return False


class TargetError:
    pass
