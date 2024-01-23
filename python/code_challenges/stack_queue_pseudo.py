from data_structures.stack import Stack

class PseudoQueue:
    """
    Class to initalize a PseudoQueue that takes in two stacks and forms a queue data structure
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Operation to add values in Stack into front of queue and reassign next to the rear node
        """
        new_node = Stack(value)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear = new_node
            self.rear.next = new_node
            

    def dequeue(self):
        """
        Operation to return values in front of queue and reassign the front to the next node
        """
        dequeue_value = self.front.value
        self.front = self.front.next
        return dequeue_value
