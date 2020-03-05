

from hamming_distance import *
import unittest


class TestHammingDistance(unittest.TestCase):

    @unittest.SkipTest
    def test_hamming_distance_0(self):
        p = 'GGGCCGTTGGT'
        q = 'GGACCGTTGAC'
        a = hamming_distance(p, q)
        b = 3
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_hamming_distance_1(self):
        p = 'GCTAAACTGTTAAAGGTAGACCCGGGACGATGTGGGGATCATCACACCGTAAAACGTATGGCGCCGCGCGGTGCTAGCCCGGGGTTCAGTAGAGGCTAATGTTTTGTGGGTGACACAATACGATTGAGCTCATCTACCCATTCACCCGTGACTATGGAACTCCATAAGCTTGCAGCTTTCAAACTCAGAAATCGAGACGGAAATACTTTTTTCAGTTACCGAGCGGAACTAAGTGTGTAGGACGGGTAGCCGGCTATACAATATCGTACGGAACTGTGTAGAGTGCCTCTACAAAATAAGGATCGAACTTTGTGGAGTGACACCGATAGTAAATCCTCGGCTAGACCCCCATGTTAAGGTCGCATACACGAGCTAACTTTCACTTCATGTTACTACTCTTCGGGGGCCCCCATAGAGTATTCGATCTACCACCGATACGTAACTGGTCGATGACGCTAAAAACGTGGCACATCTCTAGGAAAGACCACTATTACAAGGCTTATTTCCAGCGTCGAACCATTGATGAAAGGATTTCTGTGGGCCATTGTAACTAGTACGAACTATTTGTCTTTGCGTATTTTAATAATTCACTGCTGTAATGGTTCAAAGCTTAACAGCAAACAAATAGAGATACGTTATCCACTGGGAATGACATAGCCGGAAGCCCCGTGCCTATTAGCTTGCGGTAGGCTTCTAGTGCCAACGAAACGCGTCACAGTAAATCCCAGCGCGGAAAAACGCCTTAGTCGAAAGAGGGCCAAGTCGTATGTATCGGTTGATCGCTTCAGCCCTGTCCCTTTACTTGTCCAAATGCAATGTGATGCGGTGCTGGCATCGGTGATTCAACTGTGTACTACGGTATGAAGAGCCCAAAGGCATCCTGCGCTCTTCACTCAATGACCACCTTGCTCACGGTTTGAACTATGAACAGGGTACGCTCAAAGATAAATCTAAGTAGGACGCCACTCATAGATGCTAATATGATCACGGCAACAATAACTGAATTAGGCGTGGCATTCCCATCTAACTGCGTGACCCTT'
        q = 'TTGAGCTAGGGGGAGGTCCTTATCGAACCGTGGAAGGTTCTTAATCTCGTTGTGCGCCCAGAGTAGTATTGCACCGGAAAACCTATCACTGGGATTGATGCAGGGGAGCTGCAAAATCTGTGCGGAGCGCCAGAACCACATTAATCTGGCACTGTGTTAGAAAGGCCTGACTGGGCCTCGAAGCCCCCCTTAGCCGTGCAGCGATCAAGAACAGAAGATGATCACGGCTGGTCTGTTCGAGTGTGGCCCGGGAACGAGTGTCGTAACTATGGATGAAAGTATACCCTCCTGCATCACCGGAGCTGCGAGAATCCCTGCGTTTACAATTTCAAAACCGGAAAAGATCAGCATTTTGGGAGTCAAGTGACCAGAGGTATTAATGCGATGGGGTAGAGCGAAGTAAGGCGCCACGGGGCACCTCTCACATATATGTCATTCGACGGCATGCTGTTGTAAATACGCTAGGAGCACGGCCTTGAGGCAGCGTGCGGAGCAGGTATAGCGAAGCAGGGAGATCCTACGAACGCCACTTATGCGATTGACTCACAGGCGGACTCCGTACAATCACCATCGCAGGGTCCTTCCGATAACTAGGGTCTACTGCGAGCACCTAGCACATCGTTCTAGTCGTAGACTGCCGCTCTCGCGCTCAAATTCGCCTTTCAGGGAGGTGCACCCCACGGATATAGGGCGGCATTGAATGTGTCCCACCTTCGGCCTTCGATGTGGCCTCTACACAGGCCCCGTTCTCGGCAGCTGTTGGAGCGCACTGGACGTCGTCGAAACTTGTGAAATGAAGAGGCGAGGGGTTATTCAATTTATAATCGTATAAATCGCACTGTATTGAGCGGATACGATTTGACAATGCTCTGAGAGTATGTCGTGTGGCACATATCTACAGCTTTTCCTCTGACGCGCACGCTGCGATCACCCCACCAGTAAACCCTTACTCCCACCGTCCTGGGCTTTAGATTTCAAACCTACGCTCAAGTGGTTGGCCGTAGGACAGCAGGCTAGATCACTACCACCATGTGCTATGA'
        a = hamming_distance(p, q)
        b = 769
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_approximate_pattern_matching_0(self):
        text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
        pattern = 'ATTCTGGA'
        d = 3
        approx = approximate_pattern_matching(text, pattern, d)
        a = ' '.join([str(x) for x in approx])
        b = '6 7 26 27'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_approximate_pattern_matching_1(self):
        text = 'CTGTGTCAAAGGAGTGAGAGCCTGGGGTCAAGACCGGCTGGCGATTTCTTCGTTACACAACGTCATTTATTCTCATCCACACTCTAGTGACATCTTGTTAGTGCACATGGGGTGCAAGAGGTCACCATATTAGCGGATTGAACATCCAGTCCGTGGGTGTAATACCTACTCGCAGGCCCTACTTGCCGCTGCAACATATAAATGAACAGTATGCACGGTTCCTTCACCTTAGGGCCTCCCTCTTTTCCGCAGTCACCCCCTGAAGCTTACAGTGCTATGCATTGGCCGCATCGCTTGTCTTTTTTAAGGTCCTAGTGCTACCAGATGGGTAGATTTCGGATACAAATTTCATGTGCTTTTGGAGATCAATACTGTCAAACTGAAACAAAGAAGCTGCCTCGTCTGCCTCATCCACACAGACCACTGAACGGAAACAAACGCGCCTCGGAGGCCGAGGTGCCCAGTGGGTACCACTATATAACTGAAATACATCGTATGCGAGACAGGACAGCACAAGCGTCGAGAGTACGATGAGTAACGTCTGTGGTGAGCGAGCAGATTGATGAGAATAATTCTTCAAAACGCAGACAGAGCCTCCTGCTGCTTGATCAGGGAAGTGTTGAGCCCCTTTGGAGAGAAAACCATTCTAGCAATCGTCGGGTTTTGTCCGGGTAGGCAGCATAGGATCAGTGCATCTAGCTGCACGGGCCTTATTAGGGCTGTAACCATGAGGCCCAGCGTCGGCCGATTCCCGGGCGATTTGTCGCAATCCTTCGATGGAAAGTAACAGTATCCCGGGTTCATGTATCGCGTTACCGGGGAGACAGTCTCCGTGCGGCGGAGCGGTACGTTATGGTAAGTCGTCCGATACATCCGACTATCGAACAACAGGTGATAACTAAACACCTGACCGCGCTCTGACAAAATCTTGTTTAAACATAAAGAGGGAACGACCGTAGTGCTATCGGAATAGCTGTTTTATGCCGGCAATCGCAACTTCTGCTCGTGTTAATCGGAGAACCTGGGAAGTACACGGCAACGCTAAGCCGATTCCCACTGTAGCCCAATACGGCCGAAGCCAGAAGACGTCAGGTCTCGTTGAAGGTTCATCGGTAGCCTACGTGGATCAACTACAAGGGGGGAGGGCCTCAGCCATATCGCTACCTGCATCAAACAAAATCTAAGCTTAACCATTTCAAGGCACTGCCAGATAGACAGACTCAGCCAGGGAGATCTATCTCTATGTGGACCCTGTCTTCCGAGACGCAGTCTCGCTTCCTCGTCGACTGAAAGAAACACTGAGACCCTAGAAATACTGCCGCTCACTAGTCTTGCTTTTAAGTAGATAGCCAGTCCGTACACATGACGTACTAGCAAGGAACTTTCGATGATGTCGGATATGTCCGATGGTGGAACTTGGAGGGGCATATTGCGCACGCTCTGACCTGAGAAAGCAACGGTTCGCGGAGCCACTCGTGGGCATTGGACTATCACGAACCCAGACGGCCCGCGTTCGAGCATAGTCTGGCAAGGCATAACTGTTTATTGCGATATTTTAGATGTTCCGACGTGCGTGACACTACTGAACTCGCACAGCCTTGATGGAAGAGGAGACCAACATACACGTGTGTTGTATATGGAAAAGACCCCCACCCCAAGCGCTAACTCGCCTAGATCTCGGACACGTTATCGGGCGCGCTTATTCCCTCGGGAAGCCACAAATTGATCGCTTGAGCTAAACATTCTCGCCATCTAGGTTGTGAGACGCTTTACATTTAACGAAGTAAATGAAACGCTACGACTGTAGTGACAATCAACCCCTTCGATGGTATCTGGGGCGTGAATGGGAGTAAGTGAGGTATTTGCGTCCCGGAATCTGCGATCTCAATGTCCATAGCTGGGTGCAATCGGCCGTAACATGGTCTGCGTATTCGCTGGGATGATACATAAGCCTCACTCCTCAGGCGTTGTGGTCGGCGCGCGCCTGAAGTTACATTAATCTCCGCAAGGGACCCCCCATCGGAGGATGCTATACTTCTCGGACCACACCCCGTTGTGCTAATAGGCGCAGTACGCGCTTCTGGGGTTGAATTCGAGGCGAGCGTGTCGAGTGAACTTATTACCTACTCTCGAAGTCCGGATTTGAGTTGGTAAATTGCCTCCTTACCAATGGTGTGCGTAGAAAGCGTCGTGAGCACTGGCACCGCTAGACGGGAGCGAAACGTTTGTAGCTGATATTGTTATGCCACCTAGCTCTAAACTTGCGCTTCGTTTGTTCTGATAAGGGCTTTCGACAAGAGGGGGCTTATCCGCCTATGTCGCAAAGTCGCACCTGTTACGATATTATTCGACAAACCGTTTGAGCCAGATTGAGCGCCATCTAGAACTTGCCGTTTTCCAAAACAGGCGACTAAAACCCACGCTAACTCACTACGCCTCGTTATTCTAACGCCTCTGCAGAGCTAAGGAATCGGTGTTGCGTTACTACCTCAGACTAGGATCTAGGCGTGTCTTCCCACTGTAACATTAGAATTCGAGACACGGCGTATCGGCTCAATTTTGCTAGTTTGGTAGCTGCCCTACAACGCGGGGCCCAGTTTCCTCTTCACGGGGGATACCATAGCGTACTTTTACACACAAACAATGCCAATACGTACCGTCCCCAAGTGGAATGTTGTGAACTGCCCCGTAGAGGAGGCCGCCACCGAATGAAACCAAAGTGGAGTTCAACTCGGAGATCCTCTATTCGTTTGAAGTGGTGAAGTCTCAGTTTAGGTCATTATCCCTCTCCTGCAGCGAGACCAAGAAGCGGCAAACGGCTGTGGCCCATCCTTATAGGTCAGATATACCCTGAATTGTGCGCATCATCCCCACAACGGTATTCATCGTAGAAAACATCCCACCGTTGACCGCAACCCTCGACTGAGGTCTATGTGGACCGACTGGATTCTAGATCAAAACGGCAACCGCATATCTCATTACAGCCGCCTTGGGGCCTTCGGCCTTAAGTCAGGTCGACGGCTCCTTCAGAATACCCAACAAATTACGACTGTCGCCCTCGTTACTGTATGACATCTGTAAAGGCATGTGTGTCAGACTCGGTCATCGCGGCTCTACTCTCTGGCCTCAATACCCCAGGACGTGATCCGGTATGGTGTTTTCGTATTCCGGCATTCCGGTGTGGGTTCATACCACAATGAAGGTTACTATTAGTAGCGACTTCCCCCATGGATTCCATAGCGTCGCACGTTTGTCTCCCAGGCCGGGCATGCAAGGTACGGTCGTTACTTGTGTCTCCCTCAATGTCTCACGAACCACGGCGAGCCACCAGAATATCTACAATGCGAAACAACGATGCCATCCTTGATATTAACTGCAGCAGGACTCGGCTCTGCAGAAATCTCCCCGTAGAAGTCCTTTAAGCATCTCTGAGGCTAGGTGGCGAAACTGTTCAAGCAGGGGTCTTATCAGCCGGACCACCGCCAAGACCCCACAACTGGAGCTTGGCGCCCCGCCGTTGACCAAGGATCGGCTTCGACTGGACTGAGATTTGGGCGGGCGCACGCTGCTGGTAAAATGTGTCTCATGATGGGACCTCCTGGCATAGATTAAATGCCGTCGTGGGGAAACTCAGAGAGGTAGTTTCCCGGTTATTTTAGCATCAGAACCATCCCTACTCTCCTGAAGCTGGGGCCGCATTGGGGTTCTATAACGCTACGGAGCGATCGGATCCAGCCCGACGTCTCGGATCGCAAGTAAACCCGGTCAGTGGTTATATTATGCTTCGGTCTCTATGACGTGACCTTTCAATATCCCTTAGTCTTGGTTATGTTACCCCGTTCGTAACATGGAGGGGTTGTTACTGGCAATAAGCATTTCACAGTGTTTTAAAAAGGTTTAATAGATCTAGGCAGGCACCAGACGGATAATACAAGGGCCAGCTGACCCGACTATAGGGAGGGCACGCATCCCACTTGCATACATCATAAGGATGAGTCAGACGGCAAGGCGGCCATTCGTCTTCGCTGATCTGAGAAATAACAACATACTCGCCCCACATAGCGCACGATGAGGGTATCGCCCATGCTACGTTACCATTCGTTAGTTAAAGTGAACAAGGCAAATGTTTGTCAGGGTCGCTGCGCTCATCCCTGTGATCATAGAGATGGGAGGCGGTGGTGGTCACGATGTCTACTGTACCGACTTCTTCCTGAAATCTGGTTATATAAACGGTGTTCGTCACATTTAACGGAGGTGGCAGATATCAACAACGACTAACAGGCCGTAAAAAATTACCGGATAAGCACAGGCATCTATTAGTTGCGTGGGGAAGGGAGCGACAACATAACATCGGACACGAGTCCTGGCTTCCTGAAGGTTTCTCTCCCGCTAAGTCCAAGAAATTACTGCTGCATTTTGTCTGACGGTATTCAGGTTTAAGAGGAGTCTTAGTAAGAACGTGTTGGTAGTCTGCTGTCTCTCACGAATCATAGAGTTTAAGCATCGCAGGCAACTCGCCCCTTCCCTTAGCCGGTCGCGCCTTTTCCACAATAGAGGGGCCAAGCCTATCTCGGTCGTGTGCGCAATCAGTTGTTACGAGCCGCCGACGTTAGGGCGCACGGGCGCTCGTAAACGGCTATTCATACGGCCAGGAAAGTCGGCAATCCGTCCCGGTTGGGCGATATATCTTCATGGATTCTTGGCAGGGATGCTGCACGTTTTCACTAGCTTGATACAGCTCTGACAGTGGTGAAGCTCTAAGGACCAACGACTAGCAAATGTAGGGTATAGCAAGAGGATCAGCAGTCGATCGATAGTTTCTCAAAAGGGTCTATAGATCCTACACCACGTACCCTCGAACGGATGCGGGAGGTATATTTCGGATATGGTTGCCAATCGCCTTCCCAAATATCCAGGATCTGCTCTTCCCCCCCTACGCTCTCATCATTGCTCGCGGTCTTAATGTCTACCTGGATCTCGACGCGGAAGCAGAAGGCCTAAACGAAGCAATGAGCATGGGAATGGGTAGGGTTCAGTGCGGCGTGAGGGTAGAATGCTGCTTCCTAAGATTTGTACTAGTAAATCGTTTGCCTGGTATTTTGGCATCTATCTGTCGGTTATCCTCTTTATCACCCATTCAGTTCGGAAAACCAGTCTCACTCTCCAGAACCAGGACGCTGAATTAACATATACAATCTACTAGGCTCCCCCCGCCCGAGAGTTTGGGATCCTGCCGAGAGACAAGAAGAGGCTAAGACATTGTGACCTTATGAATATAGTTTTATGTAACACTTAGGCTAACCAGTACGACGACAGGTGTCGACGCTTTGGCATAAGCATACACCATTGTCGCCGACCACGTAGATCACTGCCTAATTACCTCTACATGTTCATCATGGCTGACGAAACCCCCTGATTTGTTGTCGGGAGTCCCCCCGTACCTTAGGGAATGCAGCGAGTCAAAATAGCCCAATTGAAATTCCCGGCGCGCATCAATGCGAGCCTATACGCACGCGAAGCACTAGTGCTCGAACTTACAGGTATTAGGGCTGGGGGGCCATCTATGCAAGAAGCGATAAAGGACATTGGCGTACTCTGGCTGCCTAAGCCCGTTTTCGACGACATCTCGGGACAGTCATGGGTGAAAGACTTAATTATTCGTCCTCCGCTACGGGTCGCACCCGAACTTTCGCCGGCTTATCGGAAGCCACAAGTCGTAGGGTAGATTCGGACAAGAACCCATCCGATTATCACAATATTCAATAATTCAGGCACCGTGTCCGAAAAACTTATTTACCGCTGTTTCAAGGGCCCGAATCTGGCTGTGGATGGAATCCCAGCGGTCTTCCCGGATTTATAACCCGGTTCTGGCCCTTTCACGAATTGTGTTCGCCTGGTCTACCTATCACGCGGGAGGACGGGACACGAGCCCCTCTCTGTCGACACAACTTCCGGCCCGCTCGATGCGTCCTTGATTGACGAAGACGCTCGCTAGCATAAAACGTTATTGGTGAGACCCTACATTTTGTGTCTTCCGCACTTAAATTTGGGGACTGATCATTGAGTTACGAAACGGAGGAGCCCGGTGTAATCCCGGGAATGGGAGAGCCGTTTTGTCGACCCATGAATCGATTGATTCACCGATGTACCTGTGAACGGCCGACGGTCCACAACTCTATTCTGCAACGTCCGGAGGTCTAGGGGTAACGTAAACGGGAGAAACACTCACTTAGACGCGATTGCACAAGCACGATCTCGTAGCAAACCATACCATGTTCCACTTGCCACGGGCATGTCTGAAAATATAGAATAACGTCCACAACCTAGATTTGTCAGCAATAGCGGCCCAACGTCACTTTGCGCTGTTGTGCATTCGCTCGGTGAGCCTGAACCGCTCCTTTGAGGTAATGCGGAAGACGCCTGTTAGGGTCCATTTTCTTTGATAAAATTAAAGTTTACGCAGCCTCATGATGGCTATTGGGACTTTAGTGTTCAGAGCCCGTCGACTAACTAGTTCTCCGTGAATGCCCCATGGAGACGATCGGGACACCATTGATAAGGGCTGTGACTACCTTTTCAAACCGCGACGCGAACACGCGTAGGAACCCGGGGCGACACAATGCGGGGATTTCGAGTCGCGCGCGGGGGTGGTACTCCCCCCACGTGTGATGGAAACGTAAGCGTCTGATAACAAACCCAAAAAGCTCAAGGATTTGACCATTCTAACAATTCGAGGCGTTGCCCAGCGACGAGTGGTGGGCCCAGTCGGGCGGGTTACGTAGACCGCACCATTTGGCGCTTATGGTGCGCGAAATCGGTCTCGTCACGGAGGCCCGATACAAAGCCGAGGGTGTATGGGATTACCAACCTCTCTGGTCGACCACAGAGGATATCAAAATTCAGATCATCGCGGTGGGTCTCGACTAAACACCACGCTCTGGATAGACTCATAACTCCAAAAAGGTATGGCCAGGATGCACGTCTGTAAGACGTAATCTTAGTGCACAGATCATCGGTCCCTGACCCTAACAATCCGTAGTCTGATGAGAGACACAGAGGACATGGGCTCCAAGTCGCGCGACGGAGATCAACAACTTTGGCATTGGTCCCGCGGGTTTCTTTCACCTCGCGGTGTTATCCTTATGTGCATCCAACTACGCGGTTCGTTCCAGGTGCCGCTGAACTTTCTGCACTATTTGTAGTATTCTAGGTTTCAGTGTTCCGCGGAGATAAAATGCCCCTTCAATCACAGGGAATGCCGCCAGTGAACTGACAGCTGTCGTTATGACCGGCTGGAGCCCCGGCCCCTATGTATATCTCGGTTTCGGTTCCCAGTAACCCCGCACGGGCAACGCACCAACTCACGCCGCGAGGTGATTATGTGCTAGCTGCTTAGTTGACATCACCTCTGATGTAAACGCATGTCATATTGTGTCTCAACGAAAGTCGCGGGGGCTTGCAATTAGCGCCTACAGTTTAAAACATCCTTAGACATTAAGCTGGCATGCGATCAATCCCACGCGAAGGCAAGCTGTTAAATGTTGCCGGGCCGTTAAGTCCTTCGGAAGAATCTGTACTATACACAACTCACGGAGCGATTGGCCCGAATGTGGTCAAATGCCAGAGGAGTGATAAAAGACTTTAAAGGTCATACATGTGTCAGAGTCAATCTCGATAACCCTCCCTAGTCAATGCCGGTATTATAGGTTTTGAGTCCTCCAAGCTGAAGACGCGTACTCTTCAAGAAAGGCGGAGTACGGCAATACCTGAGCGTTCATCTACTAGTTAGTCGCGCTCTATACTAAAATCCCAGCCTAGGCGTGAAGAGTTAGATAACTCGTAACTGAAACTCTGAAAGCCCTGCAGATTGGCCATTCATGCAAGACCGGGGCAGGGTACGATTCTGCACGGTGCGCATTCAAGATGATCACTCGCATCGTAAGCCACGTTGGTTCAGTTCTACCTGTCTTGTTCAGAGTGTTCTAAAATGGAACGACATACAAGAAAATGTTGGGTTTCACCATCTCGGCTGATAGGAAGGAACAAGACCCATAGGCGCAGAGTAATGCCCCTCTCCTACTTCCACGAGAGGGCCCGTCATAAACCACATTATGGGCTCTCTTGTTTCAGCTGTATCCTCAACGTACGTCATTTTCTTCCGGATAGTATAGAGCTACACGCGTACAGGCTTCAGTTGCTCCCAGCACACAAGTAATGTAAGCTATGTAGTAGCCTCCGCTTCCACACATAGCCTGTGGTTAGTTAGTGCGGAAGCGTTATCGCCCGACCGGGCGAGGAATTTGATTATCATGAGAAGTTTGCATGTGCAGGCTTTTTGTGCTACTGCTCCATTGACAACTCGACCGGCTTGAAAAACGCCAAGGCAGCAAGCAAGGACAGCAGAAGGGAACAGTGTGCTCGTAGCCGTCCCGCGAGGGCAAGATTACCATATAAGTAACCGTTCGATGCCATCTGTTTGTCACGGTGAAACCCGATGTTCCGCAATTCTCCGGCGCCGTACCGCCATCCAGCGTAACTCTCCAAGACGAGCGGGTAGTACAGTCCACCTTTGCATTTTCCCTGCGAGTACAGCGACCTCAGTTAGTTCCTCGTCTCCACCGTGCAAGACTTGGTATCCCATGGACCCAGCACTCTGATCCTCAAGCTTGTTGCCGAAGGCATAGACTGGGCGTTACCTGATGTCGGGAGGAATGTGCGGCGGAACTCGGAGAAGCGTGCGCGCGTCCGGATTAGGCAAAATGTTGCAATTGTGTCCAAACACTCACCGAACAGCGCGGGTGATCACAGATCATTGGTAATCCCACGCAGGATTTTGCCAAAGCGCCCAGATAGGGGCATTAGCGTGTGTTGTATGTATACAAAGACCGTGGGCTGGTAGTAAACGTCTAAAGCGTGATCAACTCCGGTGCACCGCTCGATTTTCGCTAAGAGCTAGGCTTTGTCGGTGACAAAAAGACCACAGAGGTGCCTTGCGACGTAAGCAGTTTAAAAGTCTATGTGCTCCTACAGAAACATAGGAAGCCCCTGGCCTAGTCGCCAAAAGGCACTGCTCGACCCGTTATTCGGGACAGTGAAGCGGCCAGGGTCCTCGCCGTTTTGTGAACCGCATAATTGACCCCTGCCCCCATAATGAGATGCGAGGGACAGAAATTTGTGACCCCAGACGTAGCGCTGCGGCCGCGTACTAGGGCTCTCATGGGTCTGCACTTTTCGACTCGACTATACCACCTCTGCCGGAATAGATACGGGTTATGTTAATAAACGATGACAGGTTTGCCAATGCTACTGTGACGCTCACCCGACAAGAAGTTCCTGCACAACACTACATAATCACCGCTGGCCGCGTAGAGAGGTGTGATGATGGGCGTTTCTCTTAGCCAGGCAGACACAGCTCAAGAGTCTTCGCTAATCTGGGAACTGCACTACTTGCGATTAACATCCCTACGCCGATAGCCACAATTAATGACCTAGAGTAATCATACTCCTATCGGTGGTCCTCGGTCATCCTGGACGGTGATTATCGCGGGGGCAAGTTTGAGAGTTAAGATATGAACGTAAGGCCTAGGCACCTCATCGATAATCGGGATAATAGTCGATTCTGCCTCGGGGGTGAGCTTACACGCGTGCCAACGTGGCACTCGCCTCTGAGCAGAAGAAAGACGTTCTGGGCAGTCAAAATCATCGACGTATAGTTTGAGTCTGGCCTGGTTCTTGAAGGCGGTAAACTTATGATGCAAACCAGAGAGCGCATGATAGCCGATAAGGGCGAAGTGGTCTAAGTAACCCTTCGCACCTCCACAAAGAGATGTTAATAAACCGCTGGTAGGTTCGACTCCTAATAGGGAGTTTATACATTTCACACAGCGTTCGGCAAAGTTTTCGTGGAGTCAAAGTGCGCCTAATGCAGACGTTACCAACCAAGTCTGGAACAAACACTCGGCCACATGACGCGACGTGGTGCTGTGATTCCTTACTGGTAGACATCGACGCAAGCTACGGCCGACCGCCAAGCCTACGCTCCAAGGGCAGACGGCGGCCTATTCCCCTCCGAGTACAAAAGATGACGTTTACAGTGAGAGTTCCAGTACAGTATTCAGCAAGATTTCTGTAACACTTCACTATCGTCCCAGCGCGAGGGATTGTAAGGTGGCTACATTACACAACCTGGCCGCCTTCAATTGCACTGGGACGCGTCGTGTAGTTTCTGCTCTGCAGTGATAAAGAGTATTGGCTTACTCTAGTTTTGTACCTCTGCGCTACCCCCGATCAGGGTTGGTAATCCATAGGAGATACTATGTTGTTGTCAGGTGGTAAGAATTGCAAAACTTTGTATAACAGTGTACGGCTAAACATCCAAAAAGGGGGCGCTTGCCAAAATCCAAACTGAGTGCGTTCACCCTCAACAGTATAGATTGTCTCTGGTAGTTACACAAGAAGTGTAGTGACTTACATAGCTGCTCTAGTAGGTATTGCTGCATAATCATAGCTAGCCTTGAAGCGATCACGCAACAAACCTGGTCCTCTCTAACTTCTAGATTTCCTTGGAATGCGACGGTAGTCGGGGTTTTCATTATGGCTCATAGCACAGCCGACATAATGTAAAGCCCTGCCTTCAGTGCGCTGTTACTAGATGGGCGAACAGCTAGGTGGCACCAACCGTCTCGCCAGAGTCTGCCGGCGATTGCGGTTCGTCGAAGTAATTCCTCATGTCCTGTTTTGTGGAACTAAAGATTGGTCAGTCTTTAATCTACAGTATTTCTTTTTTTTATAAATAATACAAGTCATTCAGTCTATCAGTAACCCGAAATGACAATAGTCTATAATCTATGTCAGAACGTTAGACCGTAACTCGCCCCAGGGCCTTGGGGGCTGCTTTATGACACCTGTGCCAGCCCCAAATCGTGTACGAAGAATGTCGAACCACCTTAAAGATCCACGTCTTTAAAGGCCTGAGTTCCAGAAGTGTTGCCTCTTTAACTCAAGAGCTCAGGGACCAAGGTGGGGAGCAACGACAGGACAATGTGATTATTGCCTACTCACTCACTAAAACCTTGCTGTTTAGCTCGTAGACAACATAACAGCTACGATACGATTGGCGTACTGTAACGACCCGAGGCGGGTGGCAAGCAGCAACAAGCAGCCGCGGTTATTAGAACCCTGGGTACCTCTATTTTGATGCTATCTTCCCGAGCGAGACGGAAACTCCCGCCGTCACCTTAAGTCCATCCATGGTTGGAACTTAATACGGTCTTTCCATTAGTGGCTGTGTACGCAACAAACTCTCCCTAATCTCCAACTGATCTCACTCTCCTCGGGATGCGGGGACAGGACACAAGCGCAGCTAGTTCCCGGTGGGCCAGCCTGCTAGACACTTGGTCTGCGAGTTCGAGGTAGTGCCATTGCTAATCAGCGAGTGAAGGTGACAGCGCTAGAGGAGGATGCTAGAATGCCTCCCAAAGTAGATAAATAGCATTGAGGGAATCGGCATTAGGGAGCGCAATAGCAGTTAACTCTTGGCACCGTGTGACGGCCCTGAACTGGGTATGGCTCTTACCTACGCCGATCAGTCCGCTCCACCTGGAAAGTAAGTAGCCGAAGGATTTTTTTGAAAGGTTGCCACCTGACGATTAATTAAGTAGTCAGCCATACAAACCAAACCGGTGACTGAGACACACTACCGCGCGACAGTTTAAGCGGGCCGTTGCCCTGTAATCGCCATCCGCTGTGCTCGGTCGTTAGATATACAATGCTAGGATAGAATGTAGGTGGTACCAGTACCCCTTAAGCTGTTGTAGAGAACGAATAAGTGTTACGTTGATTCATTCATCGAGATCATTGTGGGGGATGTAAGCCTGAATATCAGATTCGGTAGGACCGACCGTGAGTCGCACATGCCTGTGCTCTGCCCGTGACGTATTAAGAAGGGATAGCCTTGAGGTGCTCTGGTAATCAGAACAATAGAATTGTAACTGCTTGTGCAATACGAGTATGCCCCCTAAGCAATCGGGACTCTCACCTAGTAGTCTGGTACTGTCAAGATGACCCCGGTCCGCGGCGACAAAACCGAAAGGGATTTGCCGAGTTGTGACCTCGGACTTAAGGTGCACACAGGGGCCTAACGTGGAGTCACGAGTTCAAAGCCACGACACTTAAGCAGAAGCAATTGTAGTAGGACCACCATGGCTCTCAACTAAAGGACCAAGTAAGCTATTGCCGGCACCAAGTTGATTACACATCATCTGGATTCCGCGTGAACCGCTGTATTGCCGAGTTCGCACGAGTCCATGACGGCTCCGTTGGTTTGAGTCCACTACCCAAAGCTGTGCGGGTGGATCCCTCAATTGTCCTATGAGCGTCACGTTTTGCGATAGAAAATACCGGTGGTTAATATATTTATGATGTACCTGCGAAGCCTGACGAAACAAGCTAAGTATCGATCTGGCTTAGTAAGGTTCATGCGTTAAATTAAGTTCTTATGACTTCTGTAGGTTTACGACATCTAGCGTGCCCGAGTCCGTAAACTCTGGGTCTGAAGGATCAACATCTGATGGGTCTCCAAATGCAGGTTGTACTTGTAGGATGTTAGCCTGCTTAAACAAAGGACGACCGGACTGTTTCGTCCTGAATTCGTAGAATGTATTCATGGTGTCCAGCCTAACACTCTGGTTGAATATCGTCAAAGCCGGTCAATGTGCTCGCAAACGGCGCCTACGTCCCGTGTGCAAACAACAGAATCCGTGCCATGGCCAGCGCTAGCACCCGTTAAGTACCCATAATGTACCCTATGCCTCGGACCCTGGCCATACAACACGGGCATGCGCTGAGATGTAAGGCAGGAGTGGTAACAGGTCTTCTCCTTTAAGAAGAATCCTAGTACGCGAGGTCAGACTTTGGTTAGCCTCTCTAATTCATCGGGGATAACGTGCAACTCATGTTGGAGTGTAGAGGAGCCATTTTAGGAAGAAATAAGTTGCCGGTGTCGTGATCCTATCCAAGATCGCTAAGCTATCCTAGTTGCAGTAGATAGGTAACTTACTACCTGGGCTTACAGGAACACTCGGAAAAAGTATTTATGAGGATGAATAAACCATTTTAGCACATGGCTGACGTAGCCTCAGACTTACCGCAAATAAAGAGCGCCGCTAGGCGTTGTCCAGGCACTCACTTAGCTAGCACGAACTATTTGTCTCTATAGAAAGCTTCTCAGATTGAAGGTCCGAATCAGGCCCGTTGCTCTCCCATCCCACAGATGCCTCATTTTAGTGGATGCGAATGGTCCATCTCCTGCCCGTTCTAAGCGCCCGAATTTCGAATGATTCGGTCAAAATCTTAAGCTACCTATTTTGCAGTTAGGCCCTATGTGTCCTCGGTAAGAGTGACTAAAGCAATATTCGTCCGCACAAGTTCACAGGTGTCCAAGGACTGCGGTTGGTGGTCAGTAAAAGAACAAAAGAAGTCCGGCATAAAAAGGTGACTAAACCAGCCGCCCCCGCGGCTACTATATCAACCTGGAGCTTACCATGCAATCAACAGGTCACTCGGGTCCTGTACATCCGCTATGATCAGGACGTTTGTTCATGAGTCCTCTAGGTCCTTTGGACTCTGACACTGGCCCGATCTCGGAATGATTCTCGTCACAGATAAGAGGCTATATGTCGGGATGCCCTAACACGTCCAAGCGGGCCGTGCTCTCTAATAAATTCTGGGCTCATACATAAGCCGGATAGGTTCTCGACTTAGTTACAGCTGCCTCGACCAACAGTACAGGGACGCTATATTGCTACGAGTCTTGGCATAATAAATTTATGTTTAGGGGTAATCTAATGGCCCGTGGAACACTCAGTGTTTCCACGCTGAGAGCGAGATGACATTGTACTTTATCGGGATACCTTCAACCCCCTCAACAGGTACAGCATACGTTGAACTGGGGTATATTAACAGACAAACCGAACTTGACTCCATATGCCCATATCCTCCCCCCGGCCCCGCTTTCCGTTCTGCTTTAACGATACGAACGTTGTGTCTCAGGGACTACAAAGGGCCTTTCATTACGTACGTAAGATCCATCTACGTTAGGACACGTTGCCCCTGGCCCGCTTAACGGACGTGATAATTACACTCTTGTTACTTAAGGACTTATACGCTGGAGTCACGCTTTTTGCTAGCCCCCTGGTGAGGTTGTCCGGTAATAAGTATCCGCGGGCCCTTCATTTGCGAGGATTATTGTTTGTGATGGATAGAAAGTGAATTGGGAATGACTGGGGGTCATATCCACTTCGTGCACTTCCCATAAGTTCATTGCCGGAATGGCAGCGGCTAAACAGGGCAGAGCTTCTCTACTATGCTTCTAGTTATAGCGTCTTTTAGGATGTTAGCAGTTGGGCATTACTGTGGAATGATGTGACGTGCGCTCCGTGAAGCGACGCAGCACGCGTCTACTCTTGTTGTTGTCGGTAGCGAACGGGGCGTATGGGAGATGCCTCGGTAATTCCCCCGCGATGTTCGAAGCTTTCCCACCTTGTTACCCTCTGCGGTTTACTGTTGTGCACTCCTACGAAGCACATTGCCATTCAGCCAGGATCCGACCGGCTCAAGGGAGTCGATGGTTCCACAAAAGCAAGACCACAGGAAGGCTGTGGTAGACGGCTGTATAAGATCGGACCTCTACATAAATACCACACTACGAAATACTTCATCCTCTGTTGGTCCCGATACCCTCCAGGAAATAGTCGCAGGATATTAACACATGATACAAGCCTTGTGGCAGAGTTCCGCTCGAAGGCTTTCTTTAAAAGTTACTACTTTATTGCTAAATCCGACTACTCAGCGATAGCGACGCCGGAAGTCCACGCGGGAGGATGTACGTCGCCGTGTAACACGTCCGAGATTATCGAATCCTGATGAGAGTCAGGAAGCCGGAGGGCAATTATCTCGCTCTCCAGCATAGCATAGCTAATGGGATGCATGCCCGTGACCGAGTTTAGCTCTGGGAAAGTCGATGTGAAAACCTGGGACGCATTATATTAAATATATGCAGTCTAAGCTCAACCTCGAGGGAACCATGTATCGCGCCACCTGGCCTCCGTCTAGGGAACACGGCCGAAATACTACACTTTACTAGCGTGGCAAATTCAGGGATACAATCACCATAACCAGGTGGCGGGAAGGACGGGACTCCTTCTCATGGAGGGGGAATTCAATCAGGGGTGAGTGCTCTTAGGCAATGAGGGGCAGTGCTCCTAGCCTGGCAATACCCTTCCAAGTAACATCAAAGGTTGTCACGATCCGGTGCTATAGAAATTATCTGTCATTTAGCGTACGACGTACCAAGTGAGACGCTTCGGACCCGTCTGGCATCGATGCCATATGCCGAGGCGTTTGTCCTTTCGCAACGTCGACTGCCCTAAATCTCACGGAGTATGAGAAAAAACGTACCCTCTATGAATCTTCACATAGCCACCGGCAGAATGGTACGTTAACACCCGTTGAGTTCTATGGTGCGACCATGCCAAATTCAGGGTAGAGAGATGGGCTAGGGGAGCTTACTTCTCATCATACCTTCGAGAGTGTACGCGCTAGTCTCTGCGTGAGGTTTGGACTTGTTCGTAGTATACGAAACCATCTAGCTGGCAAGCGGATGGCAGCCCATTCCTGACGACCAGGGTGTCGGCACTATTGCACAATTCCTCAGAAACACGATCATGTTGCGTCACCAATCCAGCATCGGGAGCTAGTGACTAGTGCGTCGACTTGCATACCTTCACCCTACCATCTCGTTCTGGAGTAATAGATTCGTAGGAACCTTCTTGGGACGTTGGGCGGAAAGTAAGTCGTGACCTCTAGGGGTATGAGCTAATTGTGAGTATAGTAAACGCCGGGTTAGTGTAGAAGATGATGGCGACAATGCCCAGAGCAATAAAGCACCATGGGCCCCGATACTACACGTCAACTTAGTACAACCAAGTGCTGTGGTCTTCACTGCCCCGAAACGTATGCCGCTGTCTTACGCATCCGATCGAATACACCCATTAACACGGTAGCTTGAGGAATCTATACTGCGTCAACGAGCCTAACCCCTCCCGTGCCGTATTTCAGTTATGGTTCGCCCAACAATATGGGTCTTACGTGATGTATTCTATACACAACGAATCAGAGCACATGATAGCAACTACACGTCAGTGTTCCCTGACTGGGCTATAAGGCGCAAACAATTCTCATCGATCTCTGAATCGTCGTTGAACTAATGTGTCACTAAACAAGAGGGCTTGTATCATCGAGGCCAAAGTTGCCAAGCTAGTTAGCCCCGCATATGTACCGGGGAGCACAGCACGAGAGACAAACACTCTCTGCGTACAACTCGAGATCCCGATAACCTTTTTAGTTTGCAGGCTCCAGTACGTGAGCACGTGGAAAGTCCGATAAATAGTACGGCTCGTGCCCGCGATATACTCGTCTACCGATCATCACCAGCCAGCTCTAGAATGAAGAATAATACCGAGTCCAAGAACTCCGACAAGCTGTTACGGACAAACTCAATTAGCTCGATATCGGTAGGACGACAGCAGGCCGATCCGCGCCTTGTACTGCCGAGGTCTCAGTTCCTTGACGCAAACGCTTCAAACGTGGGTGGAACTTCTTCATTGTGGACGAGTCGGAGCTATCAGTACATACTCACCGAATGACTGAGTACAAGCTCATGGGGGGACGTGTTCGGAAAGCCGAGGCCGTCACGGACTTATCTATGAAGAACGTCTCAGAATAACTCCACCATCTATTTATTACCGAGTCCGACTTTTTTGTCCCTCTCCAATTATGCCCTGTAGCGGGTC'
        pattern = 'TGTAGCGGGTC'
        d = 6
        approx = approximate_pattern_matching(text, pattern, d)
        a = ' '.join([str(x) for x in approx])
        b = '3 5 9 18 27 29 36 53 82 92 95 101 103 112 128 140 144 148 157 160 167 180 183 189 196 202 209 210 211 227 243 260 277 281 286 288 300 301 310 316 331 356 365 388 392 394 401 424 433 435 442 449 455 459 476 482 487 493 498 517 531 533 538 542 544 546 550 560 586 595 598 604 605 615 617 619 628 630 645 652 654 662 663 664 670 677 682 685 690 694 699 700 709 711 720 728 731 740 746 747 761 777 782 788 790 803 805 810 811 818 825 833 838 851 854 883 907 939 954 960 968 974 977 978 979 981 997 1008 1016 1027 1041 1042 1057 1073 1084 1086 1096 1097 1105 1111 1117 1122 1131 1132 1136 1137 1139 1153 1186 1193 1209 1211 1239 1243 1245 1254 1267 1273 1313 1320 1329 1337 1340 1344 1369 1382 1384 1388 1389 1391 1398 1405 1410 1415 1417 1427 1430 1452 1459 1464 1471 1488 1493 1497 1503 1518 1523 1533 1541 1543 1554 1560 1565 1567 1583 1602 1603 1626 1628 1631 1637 1660 1684 1685 1687 1689 1691 1703 1722 1730 1751 1755 1760 1774 1788 1802 1813 1820 1822 1827 1829 1831 1833 1840 1845 1860 1865 1892 1902 1912 1913 1919 1926 1929 1965 1968 1971 1974 2003 2034 2063 2069 2070 2077 2078 2092 2093 2095 2097 2102 2104 2118 2127 2142 2149 2151 2170 2177 2179 2186 2193 2198 2205 2207 2212 2217 2226 2238 2259 2278 2279 2293 2295 2296 2299 2316 2324 2327 2333 2359 2360 2367 2369 2379 2381 2385 2444 2455 2461 2465 2466 2472 2474 2491 2496 2500 2501 2519 2539 2544 2557 2566 2569 2580 2582 2603 2604 2605 2618 2652 2665 2672 2675 2677 2687 2689 2692 2720 2729 2732 2741 2750 2751 2757 2762 2770 2791 2804 2811 2817 2820 2830 2844 2851 2855 2905 2919 2928 2932 2934 2979 2985 3005 3012 3013 3043 3050 3065 3076 3083 3088 3093 3101 3103 3115 3117 3130 3136 3141 3142 3148 3150 3161 3163 3176 3177 3211 3233 3235 3240 3253 3257 3282 3284 3286 3303 3305 3310 3315 3374 3381 3406 3418 3429 3433 3437 3442 3451 3453 3454 3466 3467 3497 3502 3504 3524 3533 3539 3549 3550 3551 3563 3570 3572 3577 3579 3584 3609 3616 3619 3621 3637 3641 3642 3654 3657 3682 3688 3694 3696 3707 3712 3717 3721 3726 3730 3740 3747 3756 3763 3764 3775 3780 3790 3792 3797 3818 3830 3831 3841 3846 3848 3857 3868 3876 3887 3888 3896 3901 3905 3927 3936 3942 3949 3951 3953 3959 4002 4003 4007 4020 4057 4066 4068 4073 4075 4084 4089 4111 4126 4127 4128 4134 4160 4163 4167 4168 4170 4173 4174 4188 4190 4195 4212 4224 4226 4230 4244 4246 4249 4253 4273 4291 4312 4318 4320 4321 4325 4327 4328 4332 4352 4359 4369 4407 4410 4414 4419 4421 4427 4435 4436 4437 4453 4460 4464 4467 4469 4471 4478 4488 4496 4501 4508 4525 4532 4549 4551 4559 4566 4568 4570 4572 4577 4591 4607 4608 4615 4620 4627 4628 4639 4655 4659 4666 4672 4688 4698 4700 4701 4706 4709 4712 4723 4730 4741 4745 4747 4750 4770 4777 4779 4786 4790 4801 4810 4812 4821 4830 4832 4841 4855 4861 4864 4875 4880 4887 4909 4914 4948 4949 4965 4971 4978 4984 4987 5017 5022 5023 5024 5031 5034 5036 5040 5047 5071 5074 5077 5079 5086 5093 5098 5105 5109 5111 5145 5165 5195 5219 5224 5231 5243 5270 5284 5296 5303 5310 5315 5317 5347 5381 5389 5418 5419 5421 5441 5450 5478 5483 5493 5532 5539 5541 5544 5547 5548 5568 5589 5594 5603 5622 5626 5633 5666 5676 5687 5688 5696 5698 5705 5712 5715 5722 5770 5792 5794 5800 5802 5803 5808 5813 5817 5820 5823 5825 5834 5835 5843 5844 5855 5856 5857 5862 5863 5866 5874 5879 5888 5903 5905 5908 5913 5920 5924 5935 5947 5979 6002 6006 6008 6021 6023 6043 6045 6048 6063 6068 6073 6076 6077 6089 6095 6103 6111 6112 6124 6128 6144 6150 6157 6179 6181 6187 6194 6196 6202 6207 6208 6231 6240 6256 6266 6273 6282 6286 6303 6306 6337 6357 6363 6368 6381 6386 6387 6403 6405 6414 6420 6421 6454 6473 6475 6484 6489 6493 6505 6532 6537 6552 6553 6554 6567 6577 6597 6601 6602 6607 6617 6620 6626 6628 6630 6633 6635 6637 6639 6642 6643 6664 6676 6712 6721 6730 6731 6736 6739 6744 6751 6756 6760 6763 6765 6777 6779 6791 6793 6800 6802 6809 6814 6816 6821 6823 6842 6844 6851 6867 6871 6881 6898 6905 6908 6910 6913 6915 6936 6938 6964 6966 6972 6983 7007 7008 7014 7034 7041 7056 7058 7064 7071 7078 7097 7098 7104 7106 7117 7124 7140 7153 7154 7164 7170 7173 7197 7202 7211 7212 7217 7219 7256 7270 7283 7284 7293 7296 7312 7314 7320 7326 7333 7347 7352 7364 7380 7383 7412 7415 7425 7427 7430 7444 7446 7447 7461 7475 7494 7501 7526 7532 7539 7540 7552 7566 7585 7590 7599 7604 7639 7640 7655 7679 7689 7698 7699 7701 7705 7724 7740 7750 7761 7777 7780 7784 7787 7819 7821 7831 7838 7861 7866 7875 7881 7886 7887 7893 7902 7904 7908 7918 7927 7949 7957 7958 7969 7971 7983 7988 8006 8008 8016 8021 8038 8061 8063 8084 8088 8108 8110 8117 8122 8125 8131 8154 8164 8166 8168 8180 8189 8215 8224 8227 8246 8253 8257 8261 8263 8269 8277 8283 8316 8323 8325 8333 8338 8359 8369 8382 8398 8406 8419 8425 8427 8453 8477 8485 8495 8497 8505 8506 8510 8516 8526 8531 8545 8578 8585 8587 8600 8603 8605 8614 8631 8640 8660 8667 8670 8681 8691 8697 8698 8700 8712 8714 8729 8735 8760 8764 8769 8788 8790 8793 8800 8846 8848 8857 8859 8864 8866 8869 8875 8887 8905 8907 8927 8947 8957 8958 8960 8978 8986 8996 8997 9013 9033 9037 9040 9062 9071 9079 9090 9092 9097 9107 9115 9120 9133 9153 9155 9175 9185 9190 9193 9201 9203 9212 9217 9227 9241 9250 9261 9262 9284 9302 9307 9309 9322 9328 9352 9364 9366 9376 9379 9381 9393 9404 9411 9413 9421 9433 9445 9504 9506 9513 9522 9526 9528 9537 9539 9541 9545 9553 9574 9585 9597 9608 9620 9622 9636 9638 9646 9653 9671 9675 9681 9684 9706 9708 9710 9714 9715 9719 9721 9730 9733 9750 9762 9772 9786 9787 9799 9806 9835 9839 9845 9858 9898 9899 9909 9923 9934 9964 9966 9971 9976 9979 9989 10015 10045 10048 10087 10089 10092 10098 10104 10113 10127 10138 10143 10146 10161 10163 10180 10200 10205 10210 10215 10217 10220 10231 10237 10239 10244 10262 10265 10278 10284 10291 10302 10316 10319 10320 10322 10323 10351 10359 10376 10377 10381 10383 10404 10405 10425 10427 10429 10434 10438 10441 10456 10458 10470 10479 10482 10486 10488 10502 10513 10514 10530 10544 10551 10563 10568 10570 10574 10576 10577 10589 10592 10599 10618 10620 10632 10642 10646 10662 10673 10680 10682 10691 10693 10700 10703 10713 10716 10721 10728 10733 10735 10751 10767 10769 10793 10805 10810 10816 10828 10846 10857 10859 10864 10871 10881 10882 10885 10898 10905 10916 10923 10927 10934 10950 10961 10979 10982 10984 11004 11017 11018 11020 11070 11078 11094 11117 11122 11127 11132 11134 11139 11156 11159 11191 11202 11207 11237 11260 11276 11279 11301 11312 11335 11336 11341 11352 11357 11364 11367 11368 11388 11396 11397 11403 11406 11410 11418 11426 11435 11439 11448 11450 11451 11461 11463 11491 11493 11498 11507 11511 11519 11536 11543 11554 11560 11563 11575 11584 11593 11604 11608 11625 11626 11627 11635 11651 11655 11673 11694 11696 11709 11710 11728 11744 11774 11781 11787 11788 11794 11802 11808 11811 11828 11843 11854 11856 11857 11859 11876 11885 11897 11904 11913 11917 11928 11937 11951 11953 11985 12020 12022 12039 12054 12060 12066 12085 12094 12106 12117 12125 12135 12140 12145 12170 12176 12185 12188 12210 12215 12229 12230 12236 12263 12265 12272 12280 12282 12283 12293 12304 12318 12336 12341 12342 12344 12345 12367 12369 12374 12381 12394 12396 12413 12420 12428 12450 12454 12465 12501 12502 12504 12510 12519 12525 12540 12549 12564 12566 12578 12581 12588 12594 12602 12628 12633 12649 12658 12660 12665 12667 12669 12685 12688 12698 12707 12718 12732 12751 12757 12775 12797 12806 12811 12812 12847 12849 12855 12861 12895 12910 12912 12914 12923 12928 12930 12937 12944 12953 12954 12956 12961 12966 12975 12989 12991 12996 12998 13009 13033 13036 13039 13055 13065 13090 13091 13112 13128 13151 13153 13158 13162 13171 13173 13185 13189 13211 13213 13215 13227 13233 13238 13242 13249 13279 13285 13288 13294 13303 13304 13313 13329 13333 13334 13362 13365 13382 13390 13417 13424 13426 13433 13441 13444 13447 13451 13458 13472 13499 13508 13524 13530 13546 13555 13567 13569 13579 13594 13603 13606 13617 13624 13641 13646 13653 13661 13672 13674 13685 13694 13695 13720 13735 13736 13741 13743 13759 13762 13781 13783 13794 13799 13827 13828 13829 13840 13843 13845 13859 13864 13876 13892 13897 13899 13912 13920 13921 13927 13940 13941 13995 14008 14022 14036 14041 14053 14101 14104 14110 14117 14165 14168 14177 14191 14193 14194 14198 14205 14212 14214 14215 14230 14232 14242 14245 14249 14256 14265 14276 14277 14297 14317 14329 14337 14338 14345 14347 14363 14371 14373 14383 14390 14391 14394 14397 14410 14420 14422 14434 14436 14441 14444 14446 14460 14463 14466 14469 14473 14477 14478 14482 14487 14489 14498 14524 14547 14560 14575 14582 14590 14597 14602 14611 14615 14618 14633 14648 14655 14658 14668 14673 14718 14719 14724 14725 14741 14748 14768 14780 14782 14783 14797 14808 14849 14854 14857 14867 14873 14877 14880 14884 14892 14907 14919 14931 14934 14950 14958 14963 14968 14972 14979 14991 15000 15030 15049 15056 15069 15071 15076 15083 15085 15091 15097 15104 15106 15110 15111 15137 15142 15151 15169 15176 15185 15187 15203 15205 15217 15219 15223 15226 15242 15247 15250 15255 15259 15290 15297 15301 15302 15313 15331 15336 15343 15347 15352 15357 15361 15368 15373 15386 15388 15391 15393 15398 15413 15429 15451 15462 15512 15514 15516 15532 15539 15543 15552 15579 15581 15588 15591 15604 15615 15621 15642 15650 15657 15660 15676 15678 15683 15685 15721 15723 15728 15740 15746 15750 15753 15757 15762 15772 15785 15803 15823 15830 15833 15835 15842 15845 15847 15859 15865 15875 15891 15904 15907 15957 15985 16000 16005 16014 16022 16027 16049 16056 16072 16080 16089 16096 16101 16103 16108 16114 16117 16131 16140 16150 16161 16166 16181 16194 16200 16205 16207 16216 16233 16244 16246 16251 16260 16267 16276 16287 16290 16304 16309 16313 16317 16331 16333 16338 16397 16401 16402 16411 16414 16419 16426 16442 16444 16447 16449 16473 16496 16511 16533 16539 16553 16556 16564 16570 16578 16582 16588 16600 16605 16611 16617 16628 16637 16639 16642 16646 16648 16662 16663 16668 16670 16677 16683 16706 16715 16716 16721 16722 16739 16746 16763 16765 16798 16815 16818 16832 16839'
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_approximate_pattern_count_0(self):
        text = 'AACAAGCTGATAAACATTTAAAGAG'
        pattern = 'AAAAA'
        d = 2
        a = approximate_pattern_count(text, pattern, d)
        b = 11
        self.assertEqual(a, b)

    @unittest.SkipTest
    def test_approximate_pattern_count_2(self):
        text = 'GGGTACTGGGCTATAAGGGGCTGTCGGAGTTTGCTGAGCAAAGCCGCTTTTCGACGGCAATTCGGCTCACCTCAGACTACAAACGCCCGCTGAGATACCTAGGTGTATTTCCTGTCCAGTTAGACTTGAGTACACTTGGCGAAACCATAGACTCTGCGAGCAGTTACGGAGATCCCATTGGTGAACTTATGATCACGAAGCTCCCGTTAATAGCTAGCTCGAGGGAACAAACAGACGGCCTTCATCCTCCTCTCAGTAACGACCGTTCCCACGGGCCATCCGAGCGGAGTATGGATACAATGTCATAGTCAGTGTCTTAAATGAGGATCCACGAGTGACAGTACGCTCGTCTTACGCGCTCCCTTCGCTACC'
        pattern = 'AACCA'
        d = 2
        a = approximate_pattern_count(text, pattern, d)
        b = 38
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
