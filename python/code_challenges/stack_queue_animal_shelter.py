from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError

# used ChatGPT to troubleshoot my AnimalShelter class
class AnimalShelter:
    """
    Instantiates an instance of an animal shelter

    param: dog or cat object
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):

        if self.rear is None:
            self.rear = animal
            self.front = animal
        else:
            self.rear.next = animal
            self.rear = animal

    # used ChatGPT to help write this logic
    def dequeue(self, species=None):
        if self.front is None:
            raise InvalidOperationError("Shelter is empty")

        if species is None:
            return None

        # Traverse the queue to find the first animal of the requested species
        current = self.front
        previous = None

        while current is not None and current.species != species:
            previous = current
            current = current.next

        # If the species is not found
        if current is None:
            return None

        # If the animal to dequeue is the first in the queue
        if previous is None:
            self.front = current.next
            if self.front is None:
                self.rear = None
        else:
            previous.next = current.next
            if previous.next is None:
                self.rear = previous

        return current


class Dog:
    """
    Instantiates an instance of a dog object

    param: name(string)
    """
    def __init__(self, name, next=None):
        self.species = "dog"
        self.next = next
        self.name = name


class Cat:
    """
    Instantiates an instance of a cat object

    param: name(string)
    """
    def __init__(self, name, next=None):
        self.species = "cat"
        self.next = next
        self.name = name