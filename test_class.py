import unittest
from class_2 import roman_to_integer

class TestRomanConverter(unittest.TestCase):
    def test_single_letters(self):
        self.assertEqual(roman_to_integer('I'), 1)
        self.assertEqual(roman_to_integer('V'), 5)
        self.assertEqual(roman_to_integer('X'), 10)
        self.assertEqual(roman_to_integer('L'), 50)
        self.assertEqual(roman_to_integer('C'), 100)
        self.assertEqual(roman_to_integer('D'), 500)
        self.assertEqual(roman_to_integer('M'), 1000)

    def test_many_letters(self):
        self.assertEqual(roman_to_integer('XI'), 11)
    def test_subtractive_notation(self):
        self.assertEqual(roman_to_integer('IV'), 4)

if __name__ == '__main__':
    unittest.main()
