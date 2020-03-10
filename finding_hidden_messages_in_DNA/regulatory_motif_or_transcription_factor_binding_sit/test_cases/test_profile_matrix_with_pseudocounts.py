

from profile_matrix_with_pseudocounts import *
import unittest


class TestProfileMatrixWithPseudocode(unittest.TestCase):
    # @unittest.SkipTest
    def test_profile_matrix_with_pseudocode_0(self):
        motifs = ['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']
        output = profile_matrix_with_pseudocounts(motifs)
        b = {'A': [0.2222222222222222, 0.3333333333333333, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 0.3333333333333333], 'C': [0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333, 0.1111111111111111, 0.1111111111111111], 'G': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.3333333333333333, 0.2222222222222222, 0.2222222222222222], 'T': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333]}
        self.assertEqual(output, b)


if __name__ == '__main__':
    unittest.main()
