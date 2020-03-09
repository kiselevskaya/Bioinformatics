

from score_motifs import *
import unittest


class TestScoreMotifs(unittest.TestCase):
    # @unittest.SkipTest
    def test_profile_0(self):
        motifs = ['TCGGGGGTTTTT', 'CCGGTGACTTAC', 'ACGGGGATTTTC', 'TTGGGGACTTTT', 'AAGGGGACTTCC',
                  'TTGGGGACTTCC', 'TCGGGGATTCAT', 'TCGGGGATTCCT', 'TAGGGGAACTAC', 'TCGGGTATAACC']
        a = profile_matrix(motifs)
        b = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0], 'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6], 'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0], 'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
        self.assertEqual(a, b)

    # @unittest.SkipTest
    def test_entropy_0(self):
        motifs = ['TCGGGGGTTTTT', 'CCGGTGACTTAC', 'ACGGGGATTTTC', 'TTGGGGACTTTT', 'AAGGGGACTTCC',
                  'TTGGGGACTTCC', 'TCGGGGATTCAT', 'TCGGGGATTCCT', 'TAGGGGAACTAC', 'TCGGGTATAACC']
        profile = profile_matrix(motifs)
        a = get_entropy(profile)
        b = 9.916290005356972
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
