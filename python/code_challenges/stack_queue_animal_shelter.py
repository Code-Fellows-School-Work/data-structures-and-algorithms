from data_structures.queue import Queue


class AnimalShelter:
    """
    Instantiates an instance of an animal shelter

    param: dog or cat object
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name, species):

        new_cat = Cat(name, species)
        new_dog = Dog(name, species)

        if self.rear is None:
            self.rear = new_cat or new_dog
            self.front = new_cat or new_dog

        else:
            self.rear.next = new_cat or new_dog
            self.rear = new_cat or new_dog

    def dequeue():
        pass


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