

from cyclopeptide_sequencing import *
import unittest
import os


class TestcCyclopeptideSequencing(unittest.TestCase):

    @unittest.SkipTest
    def test_cyclopeptide_sequencing_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\CyclopeptideSequencing\\cyclopeptide_sequencing.txt', 'r')
        data = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()

        spectrum = [int(x) for x in data[1].split()]
        b = data[3]
        collection = cyclopeptide_sequencing(spectrum)
        a = peptides_collection_as_amino_masses(collection)
        self.assertCountEqual(a.split(), b.split())


if __name__ == '__main__':
    unittest.main()
