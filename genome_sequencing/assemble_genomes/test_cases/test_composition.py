

from composition import *
import unittest
import os


class TestComposition(unittest.TestCase):

    @unittest.SkipTest
    def test_composition_0(self):
        text = 'CAATCCAAC'
        k = 5
        output = composition(text, k)
        a = ' '.join(output)
        b = 'CAATC AATCC ATCCA TCCAA CCAAC'
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_composition_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_197_3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        output = open(data_dir+'\\output_dataset_197_3.txt', 'r')
        b = [string.strip('\n') for string in output.readlines()]
        output.close()

        text = input[1]
        k = int(input[0])
        a = composition(text, k)
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_path_to_genome_0(self):
        path = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']
        a = path_to_genome(path)
        b = 'ACCGAAGCT'
        self.assertCountEqual(a, b)

    # @unittest.SkipTest
    def test_path_to_genome_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_198_3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        output = open(data_dir+'\\output_dataset_198_3.txt', 'r')
        b = [string.strip('\n') for string in output.readlines()][0]
        output.close()

        a = path_to_genome(input)

        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
