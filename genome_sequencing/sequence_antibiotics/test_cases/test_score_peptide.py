

from score_peptide import *
import unittest
import os


class TestcScorePeptide(unittest.TestCase):

    @unittest.SkipTest
    def test_score_peptide_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\CyclopeptideScoring\\cyclopeptide_scoring.txt', 'r')
        data = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        spectrum = [int(x) for x in data[2].split()]
        peptide = data[1]
        a = score_peptide(peptide, spectrum)
        b = int(data[4])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
