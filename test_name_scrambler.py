import unittest
from name_scrambler import *



class MyTestCase(unittest.TestCase):
    def test_something(self):
        #returns the same size list
        self.assertEqual(len(scramble_list([1, 2, 3])), 3)  # add assertion here

        #edge cases
        self.assertEqual(len(scramble_list([])), 0)
        self.assertNotEqual(scramble_list([1, 2, 3, 4]), scramble_list([1, 2, 3, 4]))

        #all numbers are in the list and others aren't
        list = scramble_list([1, 2, 3, 4])
        self.assertEqual(1 in list, True)
        self.assertEqual(2 in list, True)
        self.assertEqual(3 in list, True)
        self.assertEqual(4 in list, True)
        self.assertEqual(5 in list, False)

        #make sure stirings work
        string_list = scramble_list(['David', 'Matthew', 'Andrew', 'Paul', 'Sarah', 'Elizabeth'])
        print(string_list)
        self.assertEqual(len(string_list), 6)
        self.assertEqual('David' in string_list, True)
        self.assertEqual('Matthew' in string_list, True)
        self.assertEqual('Andrew' in string_list, True)
        self.assertEqual('Paul' in string_list, True)
        self.assertEqual('Sarah' in string_list, True)
        self.assertEqual('Elizabeth' in string_list, True)
        self.assertEqual('Brian' in string_list, False)


if __name__ == '__main__':
    unittest.main()
