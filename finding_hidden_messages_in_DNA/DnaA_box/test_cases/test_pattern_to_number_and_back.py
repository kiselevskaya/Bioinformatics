

from pattern_to_number_and_back import *
import unittest


class TestPatternToNumberAndBack(unittest.TestCase):

    def test_pattern_to_number(self):
        pattern = 'ATGCAA'
        number = 912
        self.assertEqual(pattern_to_number(pattern), number)

    def test_number_to_pattern_0(self):
        number = 912
        k = 6
        pattern = 'ATGCAA'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_number_to_pattern_1(self):
        number = 5437
        k = 7
        pattern = 'CCCATTC'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_number_to_pattern_2(self):
        number = 5437
        k = 8
        pattern = 'ACCCATTC'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_number_to_pattern_3(self):
        number = 9904
        k = 7
        pattern = 'GCGGTAA'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_number_to_pattern_4(self):
        number = 45
        k = 4
        pattern = 'AGTC'
        self.assertEqual(number_to_pattern(number, k), pattern)

    def test_pattern_to_number_recursion_0(self):
        pattern = 'ATGCAA'
        number = 912
        self.assertEqual(pattern_to_number_recursion(pattern), number)

    def test_pattern_to_number_recursion_1(self):
        pattern = 'CCCATTC'
        number = 5437
        self.assertEqual(pattern_to_number_recursion(pattern), number)

    def test_pattern_to_number_recursion_2(self):
        pattern = 'ACCCATTC'
        number = 5437
        self.assertEqual(pattern_to_number_recursion(pattern), number)

    def test_pattern_to_number_recursion_3(self):
        pattern = 'CGCTCGCGAAGCAGGTAC'
        number = 27755844273
        self.assertEqual(pattern_to_number_recursion(pattern), number)


if __name__ == '__main__':
    unittest.main()
