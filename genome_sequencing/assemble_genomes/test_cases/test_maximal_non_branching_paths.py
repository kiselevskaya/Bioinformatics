

from maximal_non_branching_paths import *
from composition import *
import unittest
import os


class TestEulerianPath(unittest.TestCase):

    @unittest.SkipTest
    def test_maximal_non_branching_paths_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\Contigs\\inputs\\sample.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        data = open(data_dir+'\\Contigs\\outputs\\sample.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        b = output[0].split()
        graph = de_bruijnk_graph(input)
        a = maximal_non_branching_paths(graph)

        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_maximal_non_branching_paths_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\Contigs\\inputs\\test1.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        data = open(data_dir+'\\Contigs\\outputs\\test1.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        b = output[0].split()
        graph = de_bruijnk_graph(input)
        a = maximal_non_branching_paths(graph)

        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_maximal_non_branching_paths_2(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\Contigs\\inputs\\test2.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        data = open(data_dir+'\\Contigs\\outputs\\test2.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        b = output[0].split()
        graph = de_bruijnk_graph(input)
        a = maximal_non_branching_paths(graph)

        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_maximal_non_branching_paths_3(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\Contigs\\inputs\\test3.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        data = open(data_dir+'\\Contigs\\outputs\\test3.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        b = output[0].split()
        graph = de_bruijnk_graph(input)
        a = maximal_non_branching_paths(graph)

        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_maximal_non_branching_paths_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\Contigs\\inputs\\test4.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        data = open(data_dir+'\\Contigs\\outputs\\test4.txt', 'r')
        output = [string.strip('\n') for string in data.readlines()]
        data.close()

        b = output[0].split()
        graph = de_bruijnk_graph(input)
        a = maximal_non_branching_paths(graph)

        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
