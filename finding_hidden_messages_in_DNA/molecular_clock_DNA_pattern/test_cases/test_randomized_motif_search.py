

from randomized_motif_search import *
import unittest
import os


class TestRandomizedMotifSearch(unittest.TestCase):

    @unittest.SkipTest
    def test_randomized_motif_search_0(self):
        dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
               'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
               'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
               'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
               'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
        k, t = 8, 5
        output = loop_randomized_motif_search(1000, dna, k, t)
        a = ' '.join(output)
        b = 'TCTCGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG'
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_randomized_motif_search_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_161_5.txt', 'r')
        data = dataset.readlines()
        dataset.close()

        dna = [string.strip('\n') for string in data[1:]]
        k, t = int(data[0].split()[0]), int(data[0].split()[1])
        a = loop_randomized_motif_search(1000, dna, k, t)
        b = ['ACTGCCACCATAGGT', 'AAGCAAACAACGGGG', 'AAGAGAACAACGGGG', 'AAGGGGCCAACGGGG', 'AAGGCCCTGACGGGG', 'TCCGCCACAACGGGG', 'AAGGTGCCAACGGGG', 'TCGGCCACAACGGGA', 'TAGGCCACAACGGCC', 'AACTGCACAACGGGG', 'AAGGCCATCGCGGGG', 'AAGGCTCGAACGGGG', 'AAGGCCACGCAGGGG', 'AAGGCCGTCACGGGG', 'AAGGCAGAAACGGGG', 'AAGGCCACATGAGGG', 'AGAACCACAACGGGG', 'AAGGCCACAAGATGG', 'AAGGCCACAACCACG', 'AAGGCCACAACGACC']
        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
