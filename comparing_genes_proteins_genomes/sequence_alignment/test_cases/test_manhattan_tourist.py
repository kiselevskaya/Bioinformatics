

from manhattan_tourist import *
import os
import unittest


class TestManhattanTourist(unittest.TestCase):
    # @unittest.SkipTest
    def test_manhattan_tourist_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestPathGrid\\inputs\\sample.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestPathGrid\\outputs\\sample.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        n, m = int(input[0].split()[0]), int(input[0].split()[1])
        down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
        right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]

        a = manhattan_tourist(n, m, down, right)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_manhattan_tourist_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestPathGrid\\inputs\\test1.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestPathGrid\\outputs\\test1.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        n, m = int(input[0].split()[0]), int(input[0].split()[1])
        down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
        right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]

        a = manhattan_tourist(n, m, down, right)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_manhattan_tourist_2(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestPathGrid\\inputs\\test2.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestPathGrid\\outputs\\test2.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        n, m = int(input[0].split()[0]), int(input[0].split()[1])
        down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
        right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]

        a = manhattan_tourist(n, m, down, right)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_manhattan_tourist_3(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestPathGrid\\inputs\\test3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestPathGrid\\outputs\\test3.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        n, m = int(input[0].split()[0]), int(input[0].split()[1])
        down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
        right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]

        a = manhattan_tourist(n, m, down, right)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_manhattan_tourist_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestPathGrid\\inputs\\test4.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestPathGrid\\outputs\\test4.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        n, m = int(input[0].split()[0]), int(input[0].split()[1])
        down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
        right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]

        a = manhattan_tourist(n, m, down, right)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_manhattan_tourist_5(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LongestPathGrid\\inputs\\test5.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\LongestPathGrid\\outputs\\test5.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        n, m = int(input[0].split()[0]), int(input[0].split()[1])
        down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
        right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]

        a = manhattan_tourist(n, m, down, right)
        b = int(output[0])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
