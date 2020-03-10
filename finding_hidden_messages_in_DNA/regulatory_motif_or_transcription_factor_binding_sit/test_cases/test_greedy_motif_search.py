from greedy_motif_search import *
import unittest
import os


class TestGreedyMotifSearch(unittest.TestCase):

    @unittest.SkipTest
    def test_greedy_motif_search_0(self):
        dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
        k, t = 3, 5
        output = greedy_motif_search(dna, k, t)
        a = ' '.join(output)
        b = 'CAG CAG CAA CAA CAA'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_greedy_motif_search_1(self):
        dna = ['GCCCAA', 'GGCCTG', 'AACCTA', 'TTCCTT']
        k, t = 3, 4
        output = greedy_motif_search(dna, k, t)
        a = ' '.join(output)
        b = 'GCC GCC AAC TTC'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_greedy_motif_search_2(self):
        dna = ['GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC',
               'TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC',
               'TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT',
               'GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG',
               'GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT',
               'TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT',
               'AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG',
               'AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA']
        k, t = 5, 8
        output = greedy_motif_search(dna, k, t)
        a = ' '.join(output)
        b = 'GAGGC TCATC TCGGC GAGTC GCAGC GCGGC GCGGC GCATC'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_greedy_motif_search_3(self):
        dna = ['GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT',
               'CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT',
               'GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT',
               'AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC',
               'ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG']
        k, t = 6, 5
        output = greedy_motif_search(dna, k, t)
        a = ' '.join(output)
        b = 'GTGCGT GTGCGT GCGCCA GTGCCA GCGCCA'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_greedy_motif_search_4(self):
        dna = ['GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA',
               'TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA',
               'GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA',
               'GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC',
               'AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA',
               'AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA',
               'GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA',
               'TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT']
        k, t = 5, 8
        output = greedy_motif_search(dna, k, t)
        a = ' '.join(output)
        b = 'GCAGC TCATT GGAGT TCATC GCATC GCATC GGTAT GCAAC'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_greedy_motif_search_5(self):
        data_dir = os.path.abspath('..')
        dataset = open(data_dir+'\\text_files\\dataset_159_5.txt', 'r')
        dna = [string.strip('\n') for string in dataset.readlines()[1:]]
        dataset.close()
        k, t = 12, 25
        output = greedy_motif_search(dna, k, t)
        a = ' '.join(output)
        b = 'TGCACTCTACGG CCAAGAGGATGC GTATCTATTCCC AGGCGAAAGGAG CGGCGACAACAC AGCCGAAAAGCG TGACGAAGAGGC AGATGTATAGGC GCGACTATAGGC AGACGAAAGGCG AGTCGAAATGTG AGCCGAAGGGTG AGTCGAATAGGG AGCCGAATAGCC AGCCGAAGGGTG AGCCGAAAAGTG AGCCGAAGAGCG AGGCGAAAAGCG TGACCTCTGGAG AGTCGAATAGAG AGCTCAGTAGAG TGGCCTAAGTTG AGCCGAAAGGAG AGCCGAAGGGAG CTGCGAGGACGG'
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_greedy_motif_search_with_pseudocounts_0(self):
        dna = ['GGCGTTCAGGCA',
               'AAGAATCAGTCA',
               'CAAGGAGTTCGC',
               'CACGTCAATCAC',
               'CAATAATATTCG']
        k, t = 3, 5
        output = greedy_motif_search_with_pseudocounts(dna, k, t)
        a = ' '.join(output)
        b = 'TTC ATC TTC ATC TTC'
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_greedy_motif_search_with_pseudocounts_1(self):
        data_dir = os.path.abspath('..')
        dataset = open(data_dir+'\\text_files\\dataset_160_9.txt', 'r')
        dna = [string.strip('\n') for string in dataset.readlines()[1:]]
        dataset.close()
        k, t = 12, 25
        output = greedy_motif_search_with_pseudocounts(dna, k, t)
        a = ' '.join(output)
        b = 'GCATACAGATAT GCGAACAGGTAT GCGAACAGATAT GCTGACAGATGT GCGGACAGTTGT GCGGACAGCTAT GCAGACAGTTTT GCAAACAGGTAT GCGGACAGTTGT GCCGACAGATTT GCAGACAGTTAT GCTTACAGCTCT GCTGACAGCTCT GCTAACAGTTAT GCAAACAGTTCT GCGCACAGATAT GCCGACAGATAT GCCTACAGGTGT GCCGACAGCTAT GCCAACAGATCT GCACACAGCTAT GCCAACAGATCT GCGAACAGATTT GCTCACAGGTAT GCACACAGGTTT'
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
