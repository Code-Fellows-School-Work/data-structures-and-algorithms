from data_structures.hashtable import Hashtable


def first_repeated_word(string):
    reviewed_words = set()
    for word in string.lower().split():
        if word in reviewed_words:
            return word

        reviewed_words.add(word)
