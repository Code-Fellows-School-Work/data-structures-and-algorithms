class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
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
        if self.front is None:
            # TODO: raise an error
            return None
        # get the value
        dequeue_value = self.front.value

        # move the front pointer to its next
        self.front = self.front.next
        # the Queue has become empty
        if self.rear is None:
            # also need to update self.rear
            self.rear = None

        return dequeue_value
