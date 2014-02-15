import unittest


def runtests():
    from test_data_structures import TestHashTable

    suite = unittest.TestSuite()

    suite.addTest(TestHashTable('insert'))
    suite.addTest(TestHashTable('search'))
    suite.addTest(TestHashTable('delete'))

    unittest.TextTestRunner(verbosity=2).run(suite)
