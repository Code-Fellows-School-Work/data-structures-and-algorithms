from data_structures.hashtable import Hashtable

# Used ChatGPT to write this code


def left_join(hashtable1, hashtable2):
    result = []

    # Iterate through the keys of the first hashtable
    # keys() returns the list of keys
    for key in hashtable1.keys():
        # Retrieve the synonym from the first hashtable
        # get() returns the values of each key
        synonym = hashtable1.get(key)
        print(synonym)

        # Attempt to retrieve the antonym from the second hashtable
        # get() returns the values of each key
        antonym = hashtable2.get(key)

        # Append the key, synonym, and antonym (or None) to the result each as individual lists
        result.append([key, synonym, antonym if antonym is not None else None])

    return result
