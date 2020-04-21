

from linear_spectrum import *
import unittest
import os


class TestLinearSpectrum(unittest.TestCase):

    @unittest.SkipTest
    def test_linear_spectrum_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\integer_mass_table.txt', 'r')
        MassDictionary = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        MassDictionary = dict((y[0], int(y[1])) for y in(x.split() for x in MassDictionary))

        dataset = open(data_dir+'\\LinearSpectrum\\linear_spectrum.txt', 'r')
        input = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        peptide = input[1]
        b = [int(x) for x in input[3].split()]

        a = linear_spectrum(peptide, MassDictionary)

        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
