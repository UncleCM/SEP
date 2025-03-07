import unittest
from ToHex import toHex, fromHex, InvalidArgument

class TestTest(unittest.TestCase):
    knownValues = (
        (14, "E"),
        (171, "AB"),
        (255, "FF"),
        (1, "1"),
        (16, "10"),
        (31, "1F"),
        (100, "64"),
        (256, "100"),
        (1024, "400"),
        (4096, "1000"),
        (65535, "FFFF"),
        (1048576, "100000")
    )

    def test_toHex_known_values(self):
        for integer, hex_value in self.knownValues:
            result = toHex(integer)
            self.assertEqual(result, hex_value)

    def test_fromHex_known_values(self):
        for integer, hex_value in self.knownValues:
            result = fromHex(hex_value)
            self.assertEqual(result, integer)

    def test_toHex_invalid_argument(self):
        with self.assertRaises(InvalidArgument):
            toHex(-1)
        with self.assertRaises(InvalidArgument):
            toHex(0)
        with self.assertRaises(InvalidArgument):
            toHex("string")

    def test_toHex_sanity(self):
        # Sanity check with a few additional values
        self.assertEqual(toHex(2), "2")
        self.assertEqual(toHex(10), "A")
        self.assertEqual(toHex(4095), "FFF")

    def test_fromHex_sanity(self):
        # Sanity check with a few additional values
        self.assertEqual(fromHex("2"), 2)
        self.assertEqual(fromHex("A"), 10)
        self.assertEqual(fromHex("FFF"), 4095)

if __name__ == "__main__":
    unittest.main()