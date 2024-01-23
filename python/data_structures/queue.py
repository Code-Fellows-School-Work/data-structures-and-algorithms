from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    """
    Node class representing elements in a queue
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    """
    Queue class to intitalize and perform operations on a queue data structure
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Adds new node in the rear of the queue
        """
        new_node = Node(value)

        # if the queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        # queue isn't empty
        else:
            self.rear.next = new_node
            # point the queue's self.rear to our new node. Update the pointer!
            self.rear = new_node
    
    def dequeue(self):
        """
        Removes the node from the front of the queue and raises an error is the front is empty
        """
        if self.front is None:
            raise InvalidOperationError()
        
        # get the value
        dequeue_value = self.front.value

        # move the front pointer to its next
        self.front = self.front.next
        # the Queue has become empty
        if self.rear is None:
            # also need to update self.rear
            self.rear = None

        return dequeue_value
    
    def is_empty(self):
        """
        Checks if the queue is empty
        """
        return self.front is None
    
    def peek(self):
        """
        Peek will only review the node in the front of the queue.
        Method checks the node in the front and returns that value
        """
        if self.is_empty():
            raise InvalidOperationError()
        
        return self.front.value
