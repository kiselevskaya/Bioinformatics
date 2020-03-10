

from median_sorting import *
import unittest
import os


class TestMedianSorting(unittest.TestCase):

    def test_median_sorting_0(self):
        dna = ['AAATTGACGCAT',
               'GACGACCACGTT',
               'CGTCAGCGCCTG',
               'GCTGAGCACCGG',
               'AGTACGGGACAG']
        k = 3
        a = median_sorting(dna, k)
        b = ['ACG', 'GAC']
        self.assertIn(a, b)

    def test_median_sorting_1(self):
        dna = ['ACGT', 'ACGT', 'ACGT']
        k = 3
        a = median_sorting(dna, k)
        b = ['ACG', 'CGT']
        self.assertIn(a, b)

    def test_median_sorting_2(self):
        dna = ['ATA', 'ACA', 'AGA', 'AAT', 'AAC']
        k = 3
        a = median_sorting(dna, k)
        b = 'AAA'
        self.assertEqual(a, b)

    def test_median_sorting_3(self):
        dna = ['AAG', 'AAT']
        k = 3
        a = median_sorting(dna, k)
        b = ['AAG', 'AAT']
        self.assertIn(a, b)

    # @unittest.SkipTest
    def test_median_sorting_4(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_158_9.txt', 'r')
        dna = [string.strip('\n') for string in dataset.readlines()[1:]]
        dataset.close()
        k = 6
        a = median_sorting(dna, k)
        b = 'TTGAGT'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
