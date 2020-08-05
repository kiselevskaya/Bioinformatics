

from longest_common_subsequence_backtrack import *
import os
import unittest


class TestManhattanTourist(unittest.TestCase):
    # @unittest.SkipTest
    def test_longest_common_subsequence_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\sample.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\sample.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_longest_common_subsequence_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\test1.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\test1.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_longest_common_subsequence_2(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\test2.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\test2.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_longest_common_subsequence_3(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\test3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\test3.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_longest_common_subsequence_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\test4.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\test4.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_longest_common_subsequence_5(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\test5.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\test5.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_longest_common_subsequence_6(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\test6.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestCommonSubsequence\\outputs\\test6.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        v, w = input[0], input[1]
        i, j = len(v), len(w)
        backtrack = longest_common_subsequence_backtrack(v, w)

        a = output_lcs(backtrack, v, i, j)
        b = output[0]
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
