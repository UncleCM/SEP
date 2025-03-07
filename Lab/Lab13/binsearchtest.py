import unittest
from binsearch import binsearch, InvalidArgument  

class TestBinSearch(unittest.TestCase):
    def test_known_values(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binsearch(data, 1), 0)
        self.assertEqual(binsearch(data, 11), 5)
        self.assertEqual(binsearch(data, 5), 2)

    def test_invalid_argument(self):
        with self.assertRaises(InvalidArgument):
            binsearch("not_a_list", 5)
        with self.assertRaises(InvalidArgument):
            binsearch(123, 5)
        with self.assertRaises(InvalidArgument):
            binsearch(None, 5)

    def test_not_found(self):
        data = [2, 4, 6, 8, 10]
        self.assertIsNone(binsearch(data, 1))

    def test_empty_list(self):
        data = []
        self.assertIsNone(binsearch(data, 5))

    def test_sanity_condition(self):
        data = [10, 20, 30, 40, 50]
        key = 30
        index = binsearch(data, key)
        self.assertIn(index, range(len(data)))
        self.assertEqual(data[index], key)


if __name__ == "__main__":
    unittest.main()

