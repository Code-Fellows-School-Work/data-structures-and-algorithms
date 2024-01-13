# Used JB's class code to help write below code
class Node:
    def __init__(self, value):
        self.value = value

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
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

class TargetError:
    pass
