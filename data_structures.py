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


class BinarySearchTree():
    """
    Binary Search Tree that stores integers.
    I choose integers here to keep size comparisons simple.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.log = logging.getLogger('Binary Search Tree')

    def insert(self, value):
        if self.value == value:
            self.log.warn('Value %d already exists in tree. '
                          'Not inserted.' % value)
            return

        if value < self.value:
            if self.left is not None:
                self.left.insert(value):
            else:
                self.left = BinarySearchTree(value)
        elif value > self.value:
            if self.right is not None:
                self.right.insert(value):
            else:
                self.right = BinarySearchTree(value)
        else:
            self.log.error('Value %d should have '
                           'been identified at the root.' % value)
            raise('Error inserting value %d.' % value)

    def search(self, value):
        if self.value == value:
            return self.value

        if value < self.value:
            if self.left is not None:
                return self.left.search(value)
            else:
                return None
        elif value > self.value:
            if self.right is not None:
                return self.right.search(value)
            else:
                return None
        else:
            self.log.error('Value %d should have been found in root.' % value)
            raise('Error looking for value %d.' % value)
