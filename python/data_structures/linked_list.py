# Used JB's class code to help write below code
# Used YouTube video to help with topic understanding https://www.youtube.com/watch?v=JlMyYuY1aXU

class TargetError(Exception):
    def __init__(self, message="Target value not found in the linked list"):
        self.message = message
        super().__init__(self.message)

class Node:
    """
    Class function to create a node in a linked list

    :param: 
        value: - element stored by node

    :methods:
        next: - pointer to next node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Class function to create instance of a linked list that wraps each initalized node. 

    :param: first node in the linked list initialized to none

    :methods:
        includes: - checks if a value is present
        insert: - adds a new node with the given value as the head
        __str__: - string representation of the linked list
        append: - adds a new node with the given value as the tail
        insert_before: - adds a new node with a new value before the target value node
        insert_after: - adds a new node with a new value after the target value node
        insert_kth_from_end: - iterates through linked list and finds tail node, then finds the node with index = k then returns node value
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
        # if this list is empty, then add the new node to the the head
        if not self.head:
            self.head = new_node
            return
        # if the node doesn't have a next, then append the new node here
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, value):
        if self.head is None:
            raise TargetError("The linked list is empty")

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

        raise TargetError(f"Target value {target} not found in the linked list")

    
    def insert_after(self, target, value):
        if self.head is None:
            raise TargetError("The linked list is empty")

        current = self.head
        while current:
            if current.value == target:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

        raise TargetError(f"Target value {target} not found in the linked list")
    
    # Inputted my psuedo-code algorithm into ChatGPT and produced this method
    def kth_from_end(self, k):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        # Step 2: Check if k is valid
        if k >= length or k < 0:
            raise TargetError("k is out of bounds")

        # Step 3: Find the (length - k)th element
        current = self.head
        for _ in range(length - k - 1):
            current = current.next

        return current.value
    


