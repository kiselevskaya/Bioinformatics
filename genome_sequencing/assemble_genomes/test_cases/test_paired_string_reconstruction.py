

from paired_string_reconstruction import *
import unittest
import os


class TestEulerianPath(unittest.TestCase):

    @unittest.SkipTest
    def test_paired_path_to_genome_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\sample.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        k, d = int(input[0].split()[0]), int(input[0].split()[1])

        data = open(data_dir+'\\PairedStringReconstruction\\outputs\\sample.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = []
        for i in range(100):
            pairs = [x.split('|') for x in input[1:]]
            a.append(paired_path_to_genome(pairs, k, d))
        b = output[0]
        self.assertIn(b, a)

    @unittest.SkipTest
    def test_paired_path_to_genome_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\test1.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        k, d = int(input[0].split()[0]), int(input[0].split()[1])

        data = open(data_dir+'\\PairedStringReconstruction\\outputs\\test1.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = []
        for i in range(100):
            pairs = [x.split('|') for x in input[1:]]
            a.append(paired_path_to_genome(pairs, k, d))
        b = output[0]
        self.assertIn(b, a)

    @unittest.SkipTest
    def test_paired_path_to_genome_2(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\test2.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        k, d = int(input[0].split()[0]), int(input[0].split()[1])

        data = open(data_dir+'\\PairedStringReconstruction\\outputs\\test2.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = []
        for i in range(10):
            pairs = [x.split('|') for x in input[1:]]
            a.append(paired_path_to_genome(pairs, k, d))
        b = output[0]
        self.assertIn(b, a)

    @unittest.SkipTest
    def test_paired_path_to_genome_3(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\test3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        k, d = int(input[0].split()[0]), int(input[0].split()[1])

        data = open(data_dir+'\\PairedStringReconstruction\\outputs\\test3.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = []
        for i in range(100):
            pairs = [x.split('|') for x in input[1:]]
            a.append(paired_path_to_genome(pairs, k, d))
        b = output[0]
        self.assertIn(b, a)

    @unittest.SkipTest
    def test_paired_path_to_genome_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\test4.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        k, d = int(input[0].split()[0]), int(input[0].split()[1])

        data = open(data_dir+'\\PairedStringReconstruction\\outputs\\test4.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = []
        for i in range(10):
            pairs = [x.split('|') for x in input[1:]]
            a.append(paired_path_to_genome(pairs, k, d))
        b = output[0]
        self.assertIn(b, a)

    @unittest.SkipTest
    def test_paired_path_to_genome_5(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\dataset_204_16.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        k, d = int(input[0].split()[0]), int(input[0].split()[1])

        data = open(data_dir+'\\PairedStringReconstruction\\outputs\\dataset_204_16.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = []
        for i in range(10):
            pairs = [x.split('|') for x in input[1:]]
            a.append(paired_path_to_genome(pairs, k, d))
        b = output[0]
        self.assertIn(b, a)


if __name__ == '__main__':
    unittest.main()
