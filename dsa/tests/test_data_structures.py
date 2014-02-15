import unittest
from dsa import HashTableArray


class TestHashTable(unittest.TestCase):
    def test_insert(self):
        table_array = HashTableArray(100)
        data = range(100)
        for d in data:
            table_array.insert(d)
        self.assertEqual(len(table_array.objects), 100)
