

from changing_money_problem import *
import os
import unittest


class TestMinNumberOfCoins(unittest.TestCase):
    # @unittest.SkipTest
    def test_min_number_of_coins_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\changing_money_problem\\inputs\\sample.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\changing_money_problem\\outputs\\sample.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        change = int(input[0])
        coins = [int(x) for x in list(input[1].split(','))]
        a = min_number_of_coins(change, coins)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_min_number_of_coins_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\changing_money_problem\\inputs\\test1.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\changing_money_problem\\outputs\\test1.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        change = int(input[0])
        coins = [int(x) for x in list(input[1].split(','))]
        a = min_number_of_coins(change, coins)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_min_number_of_coins_2(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\changing_money_problem\\inputs\\test2.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\changing_money_problem\\outputs\\test2.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        change = int(input[0])
        coins = [int(x) for x in list(input[1].split(','))]
        a = min_number_of_coins(change, coins)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_min_number_of_coins_3(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\changing_money_problem\\inputs\\test3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\changing_money_problem\\outputs\\test3.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        change = int(input[0])
        coins = [int(x) for x in list(input[1].split(','))]
        a = min_number_of_coins(change, coins)
        b = int(output[0])
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_min_number_of_coins_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\changing_money_problem\\inputs\\test4.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\changing_money_problem\\outputs\\test4.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        change = int(input[0])
        coins = [int(x) for x in list(input[1].split(','))]
        a = min_number_of_coins(change, coins)
        b = int(output[0])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
