import unittest
from long_and_short_new import long_and_short

class TestLongAndShort(unittest.TestCase):
    def test_long_and_short(self):
        # Test long_and_short when the inputs are strings
        result= "The longer string is:", "five" + "\nThe shorter string is:", "six"
        self.assertEqual(long_and_short("five", "six"), result)
        result = "The longer string is:", "extra" + "\nThe shorter string is:", "in"
        self.assertEqual(long_and_short("in", "extra"), result)
        result = "The two strings have the same length."
        self.assertEqual(long_and_short("kick", "five"), result)
        self.assertEqual(long_and_short("", ""), result)

    def test_long_and_short_number(self):
        # Test long_and_short when the inputs are not strings
        self.assertRaises(TypeError, long_and_short, 1, 2)
        self.assertRaises(TypeError, long_and_short, "1", 2.1)
        self.assertRaises(TypeError, long_and_short, True, False)