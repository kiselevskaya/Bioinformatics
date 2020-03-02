

import unittest


def pattern_to_number(pattern):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    n = len(pattern)
    for i in range(len(pattern)):
        number += order[pattern[i]]*4**(n-1-i)
    return number


def number_to_pattern(number, k):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    pattern = ''
    dividend = number
    for i in range(k):
        pattern = list(order.keys())[list(order.values()).index(dividend % 4)] + pattern
        dividend = dividend // 4
    return pattern


def pattern_to_number_recursion(pattern):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    if len(pattern) == 0:
        return number
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number_recursion(prefix) + order[symbol]


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
