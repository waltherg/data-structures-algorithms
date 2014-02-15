"""Some basic data structures implemented in Python

(c) Georg Walther
https://github.com/waltherg/data-structures-algorithms/blob/master/LICENSE
"""

import logging


class HashTableArray():
    """Hash table based on array."""
    
    def __init__(self, size):
        self.objects = [None for i in range(size)]
        self.size = size
        self.log = logging.getLogger('HashTableArray')

    def get_hash(obj):
        return hash(obj)  # lazy cheat: use Python's built-in hash function

    def get_index(obj):
        return get_hash(obj) % self.size

    def insert(self, obj):
        index = get_index(obj)

        if self.objects[index] is not None:
            self.log.warn('Index %d occupied. Object not inserted.' % index)
            return
        else:
            self.objects[index] = obj

    def search(self, obj):
        index = get_index(obj)
        return self.objects[index]

    def delete(self, obj):
        index = get_index(obj)
        self.objects[index] = None

