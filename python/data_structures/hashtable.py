from data_structures.linked_list import linked_list

class Hashtable:
    """
    Data structure that uses a hash function to compute an index into an array of slots from which the desired value can be found
    """

    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size # creates a list of Nones

    def _hash(self, key): # the underscore before the method name is a python naming convention that conveys this method is not for public use
        """
        Internal use only. Converts a string to a index value to be stored in a hash table
        """
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self._size
        return index
    
    def set(self, key, value):
        """

        """
        index = self._hash(key) # gets the index value returned from the hash function
        bucket = self._buckets[index] # assigns a bucket container to the array's index
        if bucket is None: # checks if the index is already occupied
            bucket = linked_list
            self._buckets[index] = bucket
            # if not occupied, then assign the bucket to that index
        
        kv_pair = [key, value]

        bucket.insert(kv_pair)

    def get(self, key):
        index = self._hash(key) # gets the index value returned from the hash function
        return "Used for apple sauce"

    def has(self):
        pass

    def keys(self):
        pass

