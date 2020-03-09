

from exhaustive_search import *
import unittest


class TestExhaustiveSearch(unittest.TestCase):

    def test_exhaustive_search_0(self):
        dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
        k, d = 3, 1
        a = ' '.join(motif_enumeration(dna, k, d))
        b = 'ATA ATT GTT TTT'
        self.assertCountEqual(a, b)

    def test_exhaustive_search_1(self):
        dna = ['GAAGCAACCGGTGGGGAAACAATTG', 'TTAACAAAACCTACAGTGCGGCTGG', 'ACGCTAACCATAAACTTGTAGTGTG', 'GCCCATAAACAAACCCACGCAACTG', 'TCGAGACACCGGATCTAAACTTAAT', 'GCCCTAATTGTAAACCCGGTTGGTA']
        k, d = 5, 1
        a = ' '.join(motif_enumeration(dna, k, d))
        b = 'AAACA AAACG CAAAC AACCG AAACT GAAAC TAAAC TCAAC AAACC AAAAC TAACC AACCT ACCTG'
        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
