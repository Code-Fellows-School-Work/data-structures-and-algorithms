from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Data structure that uses a hash function to compute an index into an array of slots from which the desired value can be found
    """

    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size  # creates a list of Nones

    def _hash(self, key):  # the underscore before the method name is a python naming convention that conveys this method is not for public use
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
        Adds a new key/value pair to the hash table
        """
        index = self._hash(
            key)  # gets the index value returned from the hash function
        # assigns a bucket container to the array's index
        bucket = self._buckets[index]
        if bucket is None:  # checks if the index is already occupied
            bucket = LinkedList()
            self._buckets[index] = bucket
            # if not occupied, then assign the bucket to that index

        kv_pair = [key, value]

        bucket.insert(kv_pair)

    def get(self, key):
        """
        Searches the hash table and retrieves the value for a given key. If the value doesn't exist, then return a key error
        """
        # gets the index value returned from the hash function
        index = self._hash(key)
        bucket = self._buckets[index]

        if bucket is None:
            return None

        current = bucket.head  # pulling from linked list terminology

        while current:  # traveres through the linked list to find the value of the given key
            kv_pair = current.value
            if kv_pair[0] == key:
                return kv_pair[1]

            current = current.next

        return None

    def has(self, key):
        """
        Checks the hashtable for a given key and returns a boolean
        """
        for bucket in self._buckets: # data type: list of linked lists
            if bucket: # data type: linked-list
                current = bucket.head # data-type: nodes
                kv_pair = current.value
                if kv_pair[0] == key:
                    return True
                
                current = current.next

        return False


    def keys(self):
        """
        Returns a list of keys
        """
        key_list = []

        for bucket in self._buckets: # data type: list of linked lists
            if bucket: # data type: linked-list
                current = bucket.head # data-type: nodes
                while current: # loops through the linked list and appends each key to the empty key_list array
                    kv_pair = current.value
                    key_list.append(kv_pair[0])
                    current = current.next

        return key_list