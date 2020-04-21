

from find_encoded_peptide import *
import unittest
import os


class TestFindEncodedPeptide(unittest.TestCase):

    @unittest.SkipTest
    def test_find_encoded_peptide_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\RNA_codon_table_1.txt', 'r')
        GeneticCode = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        GeneticCode = dict((y[0], y[1] if len(y) != 1 else '') for y in(x.split() for x in GeneticCode))

        dataset = open(data_dir+'\\EncodedPeptide\\inputs\\dataset.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        dna = input[0]
        peptide = input[1]

        dataset = open(data_dir+'\\EncodedPeptide\\outputs\\dataset.txt', 'r')
        b = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        a = find_encoded_peptide(dna, peptide, GeneticCode)

        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
