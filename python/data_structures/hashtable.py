class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size

    def hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % 1024
        return index
