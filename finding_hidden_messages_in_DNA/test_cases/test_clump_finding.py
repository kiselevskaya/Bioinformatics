

from clump_finding import *
import unittest
import os


class TestClumpFinding(unittest.TestCase):

    def test_clump_finding_0(self):
        genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
        k, l, t = 5, 50, 4
        a = clump_finding(genome, k, l, t)
        b = ['CGACA', 'GAAGA']
        self.assertCountEqual(a, b)

    def test_clump_finding_1(self):
        genome = 'GCGGTTATGCACCGTTCAAATTAGCAAACCACTAAGCGACGTAGTCTGGATTGATTTCTCCCTACCAGTGACCCAAGACGCGTTAGTGAGTTAAGTTCATATCCAGTACCTGCCGCCCTCTGTACTTGGGCGTCCGATTCGCATGCTTACTCAGGTGGAGGACACGATAATCTGATTAAACTGAGCTAAACCAGGTGGAACCAGAAACCAGGTGGGGAGTCTCGCTTCAAGCCGTTCTTGCGATCAAACCAGGTGGTCCATTATGAAACCAGGTGGCTAAACCAGGTGGTCCAGATCCTCGAATGATGTCGGTGCACATCAAAACCAGGTGGGGTGGTGGAACGTAAAACCAGGTGGCATAAACCAGGTGGGCCGGTTCGTAAACCAGGTGAAACCAGGTGGGGTGGAAACCAGGTGGGTTACAAATTACGTTGAGATGGCCCAAACCAGGTGGTGGGCTTCACCCATGTCAACAAACCACCCTATGGAACTAAACCAGGTGGAACCAGGTGGTGAAGGCTTATCCTCAGGAAAAACCAGGTGGAGGTGGTGAAATAAAACCAGGTGGACCAGGTGGATAACCCTCGCCTCGCTTCTCAACCGAGACCTGGATAAACCAGGTGGGGTGGTCCACCGATTTTTGAGACACTAGAAACCAGGTGGGCGGGGAAACCAGGTGGCAAACCAGGTGGGGTGGACGGAAACCAGGTGGATATGTCATAAAACCAAACCAGGTGGTGCACCCCCATGGTGTGTCTTATCCGTGCGTATAAACCAGGTGGTCGCACGGCTTCCACTTGCTGAGAATAGGCCCGCAGGGTCAGTGCCATGCCCTCCGTCACTCGATATGTGTTGTAAGAGTGGTTACCCCTTCATTGAAGTCGCCCACAGCCCCACCTGCATTGCTAGACTATCACCCTACAGTAGGCCTTTTCGCCTTCTTCAAGCAGCAATCTCTTATCCGCGGATGGGCGCGGCGAGCGTGGCGTCCCCGAACATTTTTACCTAACGTGTTTTGTTGGCCGCAAGCCTTCCCTCTAGTCCACCTCAGCCATTCAGCCTAGTAGCTTTCAAGCCGAGCCTTCCATATCTAATGGACCGTCCAGAATTTCACACGTTTCACAGGGCTGTGTTCGACCGCCCGTAATGCTGTTTCACAGGCGATCGCCTTGCGGTTTTTTCACAGATCGCAGCCGATGGACATGCCAACTCGATTTTCACAGAGTTTTTCACAGCGGTTTCACAGCACAGCAGTGATTGTTTCACAGCAATTTTCACTTTCACAGGGGCCCTTTTCACAGCTCAGGGCTCTTTTCACTTTCACAGTTTCACAGCGCTCCTTTCACAGAGCGGGGAAATTTAAGGGAACACTCAAGGGAACAAGGGAACACACAAAGGGAACACAACACAACACATAAGGGAACACTTTCACAGAACACAAAAGTCCGAAATCATCAGCGGCGAAGGGATTTCACAGACAGACACTTTCACAGCGCATTTCACAGATACGTACTTTCACAGGCGTACTTTCACAGACTTTCACAGAGGACAAGCTCAATTTTCACAGACAGGCTGGATAAATTTCACAGCGGTAAGGGTTTCACAGCACACATAAGGGAACACGAATTTCACAGCAGGGAACACCTCTACGAGTAATCTATTACTCTACCTACTGAAGGGAACACACCGAAGACCTACTATTACCTATTACTCTTAAAGGGAACACATTACAAGGGAACACACTCTCTCGTCATATCTCACCTCTCTATTACTCTTAAGGGAACACCTTCTCGATCAACCTATTACTCTATGGAGATAGAGATATTCCAGACATATGGAGATAACATGGAGATATGGAGATAATGGAGATGGAGATAGCTCTTATATTTATCCTATGGAGATATGATACTATTAATGGAGATAATTCTAATGGAGATATAATTACTCTAAGAGGATGGGATCTCGGGCTATTACTCTAATGGAGATAAGCACTATTACTCTAGGAAATGGAGATATGTCAATGGAGATATGTAATGGAGATAGAGGGAGATGGAGTCGCCATTTCATAATCGCCATTTCATAGTTCAGGAATCGCCATTTCCGCCATTTCTAAGATGGAGTCGCCATTTCTACGTATGGAGATAGGATCGCCATTTCATACGACCCGTTGGATATCGCCATTTCCTCGCCATTTCTGGTGACATTTCTCGCCATTTCATTTCTGGAGATAGATGGATCTCGCCATTTCATAGGAATCGCCATTTCCACGTAGGGGGGGCCACAATCCGTAGGTCGGAATTCAGACTCGCCATTTCCCATCGCCATTTCTTCACCTGTATGCCGATCCCTTCGCCATTTCTCATGGAGATAACTCTCTCTCGCCATTTCTCGCCATTTCCATTTCACTCTCATTCGCCATCGCCATTTCCATTCGCCATTTCATCGCCATTTCTTCAGGATAAGATATCGCCATTTCGACTCTCATTCGCATACTGACTCTCATTCTCATCTCGCCATTTCTCATCTGACTCTCATCCTGGGGGAAACTTGCGACTCTCATCACACTTCCGTCGACTCTCATACTGGCGGATAGCATAGGAGCCATTTAAAGACTCTCATTCTCATTCGAGACTCTCATTCAAATCCTACGAGGACTCTCATATAGACTCTCATATCATTACGAGGACTCTCATATACGAGCCATGCATGTGGCGACGACTCTCATCTACGAGCCATGCAAGCAGAATCTACGAGCGACTCTCATTACGAGCCATGTGACCGTACGAGCCATGCATGCATGCCATGCTGACTCTCATCGAGTACGAGCCATGGAAGTTCTTGTTGGTTCGTAGCCCAAGAGCTGAAGTTACGAGCCTACGAGCCATGAAGTTACTTTTACGAGCCATGAAGCTTACGATACGAGCCATGCGAGCCATGCATCCGCGCTACGAGCCATGTTCCAGTACGAGCCATGTTAGTTGCTGAAGTTAAGTTTGGCGCTGAAGTTTGTACGAGCCATGTGCCCGCTGAAGTTTGTTGTACGAGCCATGCATGCTGAAGTTAATGGCTGAAGTTAGCGTTTGCGGGCAGATCCTCATTCTACGATACGAGCCATGCCATGCAGCTGAAGTTAAGTTGGGTTACGAGCCATGCGAGCCATGTGAAGTACGAGCCATGCTGGCTGAAGTTGTTTGTGCTGCTGAAGTTGCTCTTGTCTCTAGCTGAAGTTGCCAACAGGGCTGAAGCTGAAGTTTAAGCTGAAGTTGCGAGCAGGCTGAAGTTATCGGATTGGGGCTGAAGTTCAACCTCCCGTCCCCCCACACTATATTCCCGTCCCCCCCCGCGCACGCGCCGTCTCCCGTCCCCCCTATCCCGTGCGCACGCGACGCGATCCCGTCCCCCCAGAGTGCGCGCACGCGTCCCCCTTCCCGTCCCCCTCTCCCGGGCGCACGCGTCGCTCAACATTTCCGCGCACGCGTCGCGCACGCGGGCGCACGCGGGTCCCGTCCCCCCCCCTCTTCGGCGCACGCGGAATTCCCGTCGCGCACGCGTCCCGTCCCGCGCACGCGTCGCGCACGCGACTGCCCTAACCAACAGTGCGCACGCGCCGGTAACCCGGTAACCCGGTAACCGCGCACGCGGGCGCACGCGCGTAACCCGCGCACGCGCCGCGCACGCGGCCCGGTTCCCGTCCCCCCCGGTAACCCGGTAACTCCCGTCCCCCGTAACCCGGTGCGCACGCGCCCGGCGCACGCGGAGCGCACGCGCCCCCCCCGGTAATAGCGCACGCGCCCGGGCGCACGCGCCCGGTAACCCGGTAACCCGGGCGCGCGCACGCGGCGGCGCACGCGGCGCACGCGGCGCACGCG'
        k, l, t = 11, 566, 18
        a = clump_finding(genome, k, l, t)
        b = ['AAACCAGGTGG']
        self.assertCountEqual(a, b)

    def test_clump_finding_2(self):
        genome = 'CCCGGACTTCCCCAAAAGTCCAACAGGGCGAGAACCGATTCGTCTTAAATCAAAAAATCCAAAAAACAGAACCGTACCTCGGTTTTTCACAATGTACTCGGGTCTAACTATAGGTCCAAACCGTGTATTCATGTCGGTTAGTCCATCGTGATGTTTGGTTCACTGTCTGCACTGCCCGAATCCAGCGGGCCCCTCTTCCGTCACGCTAATGTACGGGGGACAGTCCCGTTGGCGCTTTTTTAGGACAGTCAGTGGGATTGGGCAGTGGGATCTAGCGCGAACCTGCCAGAAAAGACCTTGCAGACGCGTTCGTCCGAGGAGCCACTAAGATTGACACCATGGTGGGCCCTGATTGACCTGGATATCGAATGTAGCCTGATCTGACCTGATCTGAGCGGGCACTTTGAGCACTTAATTTTTGGCCGACGGTTCCCACGCACGTCACCCACGACACCCCACTTATACTTGCTGTCGCGCGTCGAGATGACTCTGCGGGCGGTGCACTCTGCGGCAAACTGTACGGAACAGAGAACCACTCCTTCTTCCAGCGCCGTAAGCCGTAGCCGTAAACCAAATATACCAAGCCGGGTGCCCCTGCAGAGGCACACATCTGTTGTACTCGAGACAACTCGAGACAACAGACAAACGACGCCACCGTGGGATATCACCCATACCACTAGGGATAAAAGGAGTTCCTGATCCACGAATCATGACAGTGTCCATTTGATTGTATAATTTAACTGGCAGGTTGCGCCGTTTGGCAACATGACCACTCCGACGATTTCCTAGGAAAAAGCTCCTGGCAGCCTGTTTGGGACTTTAGTATTTTTAACGGCCAAGGCACGTTAGTGTTGGATTAGCTCTTTCAGCATCCTGAGGTCGGGGATCATCGATGCCCCAGCAGATGTTACTCGTGGCGGGAAAAGAGCACTTACACAGCCGGGCAGCCTGTCCGAGACGGCTTGAACGCCAGAAAGGGACCGTGTTATACTTGAAAGAAGGTTATCAGAACAAAGCGTAGACATCGAGGGGTAGAGGTTCGGAGTGCTGGCGAGGCAACCGTGGAGGAAGCCTAGGGACTGGAAGCAAATCTAGCATTCTGCTCTTGTGGTGTCTCGGCATAGGTCATATCGCTGGCTAAATGTAGACGCCACGAAGATTCAAACTCACAAGGAATTAGTTCGTGACGTAAGCGCTTCTGGGCCTGTGAATTTTAGCGATTCGGACGAATATAGTTCGATTATCGCTTCCTCACTTCCGTCTCTGGGGCGTCGAACCGGCATCCCGCCTTACAGATGGTCCGCGAACGCAGTTGCCTGGGAGGCTTCTAGGCTTGAGGCTTCTAACCACCACTCATATTCTATAACCGAGGATAACATTTTTTGCTTCGAGTTTCGAGGTATAGTAATATAATATCGCTTTCAATATCGCTTAACATATAAAAGGGGCTATTGTCGTCGTAATTCCAGGTCGCGTTTGGTCGCGTTCCTCGTTGGAAAGTATCACGCAAATTTACCGTAGTTCAGGTTGCGAAGAAAGTCGTGACGATGTGAGCCGCCCGTTTAACAAAGGCTGAATCTGGAACCAAGTGTAGCTCCCCACTTATGACGTTAAGTTAAGGAGACGGGACCCCCTGATAAGTGTATCGCGTGATTTAAGCTTGTGAGACTACTCCCCGCAAACTTGGTGTTGGAGTAACTCATGACGCCGTAATCCTTTGCCTGCCCCCCGATGCGCAAAATGCGCAAAATGCGCAAAATGCGCAAAATGCGCAAAATGCGCAAA'
        k, l, t = 9, 29, 3
        a = clump_finding(genome, k, l, t)
        b = ['ATGCGCAAA', 'TGCGCAAAA', 'GCGCAAAAT', 'CGCAAAATG', 'GCAAAATGC', 'CAAAATGCG', 'AAAATGCGC', 'AAATGCGCA', 'AATGCGCAA']
        self.assertCountEqual(a, b)

    def test_clump_finding_efficient_0(self):
        genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
        k, l, t = 5, 50, 4
        a = clump_finding(genome, k, l, t)
        b = ['CGACA', 'GAAGA']
        self.assertCountEqual(a, b)

    def test_clump_finding_efficient_1(self):
        genome = 'GCGGTTATGCACCGTTCAAATTAGCAAACCACTAAGCGACGTAGTCTGGATTGATTTCTCCCTACCAGTGACCCAAGACGCGTTAGTGAGTTAAGTTCATATCCAGTACCTGCCGCCCTCTGTACTTGGGCGTCCGATTCGCATGCTTACTCAGGTGGAGGACACGATAATCTGATTAAACTGAGCTAAACCAGGTGGAACCAGAAACCAGGTGGGGAGTCTCGCTTCAAGCCGTTCTTGCGATCAAACCAGGTGGTCCATTATGAAACCAGGTGGCTAAACCAGGTGGTCCAGATCCTCGAATGATGTCGGTGCACATCAAAACCAGGTGGGGTGGTGGAACGTAAAACCAGGTGGCATAAACCAGGTGGGCCGGTTCGTAAACCAGGTGAAACCAGGTGGGGTGGAAACCAGGTGGGTTACAAATTACGTTGAGATGGCCCAAACCAGGTGGTGGGCTTCACCCATGTCAACAAACCACCCTATGGAACTAAACCAGGTGGAACCAGGTGGTGAAGGCTTATCCTCAGGAAAAACCAGGTGGAGGTGGTGAAATAAAACCAGGTGGACCAGGTGGATAACCCTCGCCTCGCTTCTCAACCGAGACCTGGATAAACCAGGTGGGGTGGTCCACCGATTTTTGAGACACTAGAAACCAGGTGGGCGGGGAAACCAGGTGGCAAACCAGGTGGGGTGGACGGAAACCAGGTGGATATGTCATAAAACCAAACCAGGTGGTGCACCCCCATGGTGTGTCTTATCCGTGCGTATAAACCAGGTGGTCGCACGGCTTCCACTTGCTGAGAATAGGCCCGCAGGGTCAGTGCCATGCCCTCCGTCACTCGATATGTGTTGTAAGAGTGGTTACCCCTTCATTGAAGTCGCCCACAGCCCCACCTGCATTGCTAGACTATCACCCTACAGTAGGCCTTTTCGCCTTCTTCAAGCAGCAATCTCTTATCCGCGGATGGGCGCGGCGAGCGTGGCGTCCCCGAACATTTTTACCTAACGTGTTTTGTTGGCCGCAAGCCTTCCCTCTAGTCCACCTCAGCCATTCAGCCTAGTAGCTTTCAAGCCGAGCCTTCCATATCTAATGGACCGTCCAGAATTTCACACGTTTCACAGGGCTGTGTTCGACCGCCCGTAATGCTGTTTCACAGGCGATCGCCTTGCGGTTTTTTCACAGATCGCAGCCGATGGACATGCCAACTCGATTTTCACAGAGTTTTTCACAGCGGTTTCACAGCACAGCAGTGATTGTTTCACAGCAATTTTCACTTTCACAGGGGCCCTTTTCACAGCTCAGGGCTCTTTTCACTTTCACAGTTTCACAGCGCTCCTTTCACAGAGCGGGGAAATTTAAGGGAACACTCAAGGGAACAAGGGAACACACAAAGGGAACACAACACAACACATAAGGGAACACTTTCACAGAACACAAAAGTCCGAAATCATCAGCGGCGAAGGGATTTCACAGACAGACACTTTCACAGCGCATTTCACAGATACGTACTTTCACAGGCGTACTTTCACAGACTTTCACAGAGGACAAGCTCAATTTTCACAGACAGGCTGGATAAATTTCACAGCGGTAAGGGTTTCACAGCACACATAAGGGAACACGAATTTCACAGCAGGGAACACCTCTACGAGTAATCTATTACTCTACCTACTGAAGGGAACACACCGAAGACCTACTATTACCTATTACTCTTAAAGGGAACACATTACAAGGGAACACACTCTCTCGTCATATCTCACCTCTCTATTACTCTTAAGGGAACACCTTCTCGATCAACCTATTACTCTATGGAGATAGAGATATTCCAGACATATGGAGATAACATGGAGATATGGAGATAATGGAGATGGAGATAGCTCTTATATTTATCCTATGGAGATATGATACTATTAATGGAGATAATTCTAATGGAGATATAATTACTCTAAGAGGATGGGATCTCGGGCTATTACTCTAATGGAGATAAGCACTATTACTCTAGGAAATGGAGATATGTCAATGGAGATATGTAATGGAGATAGAGGGAGATGGAGTCGCCATTTCATAATCGCCATTTCATAGTTCAGGAATCGCCATTTCCGCCATTTCTAAGATGGAGTCGCCATTTCTACGTATGGAGATAGGATCGCCATTTCATACGACCCGTTGGATATCGCCATTTCCTCGCCATTTCTGGTGACATTTCTCGCCATTTCATTTCTGGAGATAGATGGATCTCGCCATTTCATAGGAATCGCCATTTCCACGTAGGGGGGGCCACAATCCGTAGGTCGGAATTCAGACTCGCCATTTCCCATCGCCATTTCTTCACCTGTATGCCGATCCCTTCGCCATTTCTCATGGAGATAACTCTCTCTCGCCATTTCTCGCCATTTCCATTTCACTCTCATTCGCCATCGCCATTTCCATTCGCCATTTCATCGCCATTTCTTCAGGATAAGATATCGCCATTTCGACTCTCATTCGCATACTGACTCTCATTCTCATCTCGCCATTTCTCATCTGACTCTCATCCTGGGGGAAACTTGCGACTCTCATCACACTTCCGTCGACTCTCATACTGGCGGATAGCATAGGAGCCATTTAAAGACTCTCATTCTCATTCGAGACTCTCATTCAAATCCTACGAGGACTCTCATATAGACTCTCATATCATTACGAGGACTCTCATATACGAGCCATGCATGTGGCGACGACTCTCATCTACGAGCCATGCAAGCAGAATCTACGAGCGACTCTCATTACGAGCCATGTGACCGTACGAGCCATGCATGCATGCCATGCTGACTCTCATCGAGTACGAGCCATGGAAGTTCTTGTTGGTTCGTAGCCCAAGAGCTGAAGTTACGAGCCTACGAGCCATGAAGTTACTTTTACGAGCCATGAAGCTTACGATACGAGCCATGCGAGCCATGCATCCGCGCTACGAGCCATGTTCCAGTACGAGCCATGTTAGTTGCTGAAGTTAAGTTTGGCGCTGAAGTTTGTACGAGCCATGTGCCCGCTGAAGTTTGTTGTACGAGCCATGCATGCTGAAGTTAATGGCTGAAGTTAGCGTTTGCGGGCAGATCCTCATTCTACGATACGAGCCATGCCATGCAGCTGAAGTTAAGTTGGGTTACGAGCCATGCGAGCCATGTGAAGTACGAGCCATGCTGGCTGAAGTTGTTTGTGCTGCTGAAGTTGCTCTTGTCTCTAGCTGAAGTTGCCAACAGGGCTGAAGCTGAAGTTTAAGCTGAAGTTGCGAGCAGGCTGAAGTTATCGGATTGGGGCTGAAGTTCAACCTCCCGTCCCCCCACACTATATTCCCGTCCCCCCCCGCGCACGCGCCGTCTCCCGTCCCCCCTATCCCGTGCGCACGCGACGCGATCCCGTCCCCCCAGAGTGCGCGCACGCGTCCCCCTTCCCGTCCCCCTCTCCCGGGCGCACGCGTCGCTCAACATTTCCGCGCACGCGTCGCGCACGCGGGCGCACGCGGGTCCCGTCCCCCCCCCTCTTCGGCGCACGCGGAATTCCCGTCGCGCACGCGTCCCGTCCCGCGCACGCGTCGCGCACGCGACTGCCCTAACCAACAGTGCGCACGCGCCGGTAACCCGGTAACCCGGTAACCGCGCACGCGGGCGCACGCGCGTAACCCGCGCACGCGCCGCGCACGCGGCCCGGTTCCCGTCCCCCCCGGTAACCCGGTAACTCCCGTCCCCCGTAACCCGGTGCGCACGCGCCCGGCGCACGCGGAGCGCACGCGCCCCCCCCGGTAATAGCGCACGCGCCCGGGCGCACGCGCCCGGTAACCCGGTAACCCGGGCGCGCGCACGCGGCGGCGCACGCGGCGCACGCGGCGCACGCG'
        k, l, t = 11, 566, 18
        a = clump_finding(genome, k, l, t)
        b = ['AAACCAGGTGG']
        self.assertCountEqual(a, b)

    def test_clump_finding_efficient_2(self):
        genome = 'CCCGGACTTCCCCAAAAGTCCAACAGGGCGAGAACCGATTCGTCTTAAATCAAAAAATCCAAAAAACAGAACCGTACCTCGGTTTTTCACAATGTACTCGGGTCTAACTATAGGTCCAAACCGTGTATTCATGTCGGTTAGTCCATCGTGATGTTTGGTTCACTGTCTGCACTGCCCGAATCCAGCGGGCCCCTCTTCCGTCACGCTAATGTACGGGGGACAGTCCCGTTGGCGCTTTTTTAGGACAGTCAGTGGGATTGGGCAGTGGGATCTAGCGCGAACCTGCCAGAAAAGACCTTGCAGACGCGTTCGTCCGAGGAGCCACTAAGATTGACACCATGGTGGGCCCTGATTGACCTGGATATCGAATGTAGCCTGATCTGACCTGATCTGAGCGGGCACTTTGAGCACTTAATTTTTGGCCGACGGTTCCCACGCACGTCACCCACGACACCCCACTTATACTTGCTGTCGCGCGTCGAGATGACTCTGCGGGCGGTGCACTCTGCGGCAAACTGTACGGAACAGAGAACCACTCCTTCTTCCAGCGCCGTAAGCCGTAGCCGTAAACCAAATATACCAAGCCGGGTGCCCCTGCAGAGGCACACATCTGTTGTACTCGAGACAACTCGAGACAACAGACAAACGACGCCACCGTGGGATATCACCCATACCACTAGGGATAAAAGGAGTTCCTGATCCACGAATCATGACAGTGTCCATTTGATTGTATAATTTAACTGGCAGGTTGCGCCGTTTGGCAACATGACCACTCCGACGATTTCCTAGGAAAAAGCTCCTGGCAGCCTGTTTGGGACTTTAGTATTTTTAACGGCCAAGGCACGTTAGTGTTGGATTAGCTCTTTCAGCATCCTGAGGTCGGGGATCATCGATGCCCCAGCAGATGTTACTCGTGGCGGGAAAAGAGCACTTACACAGCCGGGCAGCCTGTCCGAGACGGCTTGAACGCCAGAAAGGGACCGTGTTATACTTGAAAGAAGGTTATCAGAACAAAGCGTAGACATCGAGGGGTAGAGGTTCGGAGTGCTGGCGAGGCAACCGTGGAGGAAGCCTAGGGACTGGAAGCAAATCTAGCATTCTGCTCTTGTGGTGTCTCGGCATAGGTCATATCGCTGGCTAAATGTAGACGCCACGAAGATTCAAACTCACAAGGAATTAGTTCGTGACGTAAGCGCTTCTGGGCCTGTGAATTTTAGCGATTCGGACGAATATAGTTCGATTATCGCTTCCTCACTTCCGTCTCTGGGGCGTCGAACCGGCATCCCGCCTTACAGATGGTCCGCGAACGCAGTTGCCTGGGAGGCTTCTAGGCTTGAGGCTTCTAACCACCACTCATATTCTATAACCGAGGATAACATTTTTTGCTTCGAGTTTCGAGGTATAGTAATATAATATCGCTTTCAATATCGCTTAACATATAAAAGGGGCTATTGTCGTCGTAATTCCAGGTCGCGTTTGGTCGCGTTCCTCGTTGGAAAGTATCACGCAAATTTACCGTAGTTCAGGTTGCGAAGAAAGTCGTGACGATGTGAGCCGCCCGTTTAACAAAGGCTGAATCTGGAACCAAGTGTAGCTCCCCACTTATGACGTTAAGTTAAGGAGACGGGACCCCCTGATAAGTGTATCGCGTGATTTAAGCTTGTGAGACTACTCCCCGCAAACTTGGTGTTGGAGTAACTCATGACGCCGTAATCCTTTGCCTGCCCCCCGATGCGCAAAATGCGCAAAATGCGCAAAATGCGCAAAATGCGCAAAATGCGCAAA'
        k, l, t = 9, 29, 3
        a = clump_finding(genome, k, l, t)
        b = ['ATGCGCAAA', 'TGCGCAAAA', 'GCGCAAAAT', 'CGCAAAATG', 'GCAAAATGC', 'CAAAATGCG', 'AAAATGCGC', 'AAATGCGCA', 'AATGCGCAA']
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_clump_finding_efficient_3(self):
        data_dir = os.path.abspath('..')
        e_coli = open(data_dir+'\\text_files\\E_coli.txt', 'r')
        genome = e_coli.readlines()[0]
        e_coli.close()
        k, l, t = 9, 500, 3
        a = len(clump_finding_efficient(genome, k, l, t))
        b = 1904
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
