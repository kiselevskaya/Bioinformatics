

from distance_between_pattern_and_strings import *
import unittest
import os


class TestDistanceBetweenPatternAndStrings(unittest.TestCase):
    # @unittest.SkipTest
    def test_distance_between_pattern_and_strings_0(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\dataset_5164_1.txt', 'r')
        data = dataset.readlines()
        dataset.close()
        pattern = data[0].strip('\n')
        dna = data[1].split()
        a = distance_between_pattern_and_strings(pattern, dna)
        b = 38
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
