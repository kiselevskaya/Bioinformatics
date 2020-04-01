

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

    @unittest.SkipTest
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

    @unittest.SkipTest
    def test_overlap_0(self):
        patterns = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'GGCAC']
        a = overlap(patterns)
        b = {'GCATG': ['CATGC'], 'CATGC': ['ATGCG'], 'AGGCA': ['GGCAT', 'GGCAC'], 'GGCAT': ['GCATG']}
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_overlap_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_198_10.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\output_dataset_198_10.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        a = overlap(input)
        b = dict((y[0], y[2:]) for y in (x.split() for x in output))
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_de_bruijnk_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\deBruijnGraphString\\inputs\\sample.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\deBruijnGraphString\\outputs\\sample.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        text = input[1:][0]
        k = int(input[0])
        a = de_bruijnk(text, k)
        b = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in output))
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_de_bruijnk_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\deBruijnGraphString\\inputs\\test1.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\deBruijnGraphString\\outputs\\test1.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        text = input[1:][0]
        k = int(input[0])
        a = de_bruijnk(text, k)
        b = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in output))
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_de_bruijnk_2(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\deBruijnGraphString\\inputs\\test2.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\deBruijnGraphString\\outputs\\test2.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        text = input[1:][0]
        k = int(input[0])
        a = de_bruijnk(text, k)
        b = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in output))
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_de_bruijnk_3(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\deBruijnGraphString\\inputs\\test3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\deBruijnGraphString\\outputs\\test3.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        text = input[1:][0]
        k = int(input[0])
        a = de_bruijnk(text, k)
        b = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in output))
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_de_bruijnk_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\deBruijnGraphString\\inputs\\test4.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\deBruijnGraphString\\outputs\\test4.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        text = input[1:][0]
        k = int(input[0])
        a = de_bruijnk(text, k)
        b = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in output))
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_de_bruijnk_5(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_199_6.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        data = open(data_dir+'\\output_dataset_199_6.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        text = input[1:][0]
        k = int(input[0])
        a = de_bruijnk(text, k)
        b = dict((y[0], y[2:]) for y in (x.split() for x in output))
        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
