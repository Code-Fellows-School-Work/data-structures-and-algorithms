class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size # creates a list of Nones

    def _hash(self, key): # the underscore before the method name is a python naming convention that conveys this method is not for public use
        """
        Internal use only. Converts a string to a index value to be stored in a hash table
        """
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self.size
        return index
    
    def set(self, key, value):
        pass

    def get(self):
        pass

    def has(self):
        pass

    def keys(self):
        pass

