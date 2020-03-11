

from gibbs_sampler import *
import unittest
import os


class TestRandomizedMotifSearch(unittest.TestCase):

    @unittest.SkipTest
    def test_gibbs_sampler_0(self):
        dna = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA',
               'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
               'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
               'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
               'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
        k, t = 8, 5
        n = 100
        output = gibbs_sampler(dna, k, t, n)
        a = ' '.join(output)
        b = 'TCTCGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG'
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_gibbs_sampler_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_163_4.txt', 'r')
        data = dataset.readlines()
        dataset.close()
        dna = [string.strip('\n') for string in data[1:]]
        k, t, n = int(data[0].split()[0]), int(data[0].split()[1]), int(data[0].split()[2])
        output = gibbs_sampler(dna, k, t, n)
        a = ' '.join(output)
        b = 'AAGCATTGCGTAACG GCGAGTCCCGTCACG ATACTGCCCGTCACG GACGTGCCCGTCACG GCGCTGCCTTACACG GCGCTGCCCGTGCTG GCGCTGCTACTCACG GCGCTGCCCGTCGAC GCGCACGCCGTCACG GCGCTCGACGTCACG AAGCTGCCCGTCACA GCGCTGCCCGATCCG GCGCTGAGTGTCACG GCTGAGCCCGTCACG GCGCTGGTGGTCACG ACGCTGCCCGTCATC GCGCAATCCGTCACG GCGCTTAGCGTCACG GCGCTGCCCTCTACG GCGAATCCCGTCACG'
        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
