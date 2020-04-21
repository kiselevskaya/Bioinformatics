

from RNA_into_amino_acids import *
import unittest
import os


class TestRNAintoAminoAcids(unittest.TestCase):

    @unittest.SkipTest
    def test_rna_into_amino_acids_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\RNAintoAminoAcids\\inputs\\dataset.txt', 'r')
        rna = ''.join([string.strip('\n') for string in dataset.readlines()])
        dataset.close()

        dataset = open(data_dir+'\\RNA_codon_table_1.txt', 'r')
        GeneticCode = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        dataset = open(data_dir+'\\RNAintoAminoAcids\\outputs\\dataset.txt', 'r')
        peptide = ''.join([string.strip('\n') for string in dataset.readlines()])
        dataset.close()

        a = rna_into_amino_acids(rna, GeneticCode)

        self.assertEqual(a, peptide)


if __name__ == '__main__':
    unittest.main()
