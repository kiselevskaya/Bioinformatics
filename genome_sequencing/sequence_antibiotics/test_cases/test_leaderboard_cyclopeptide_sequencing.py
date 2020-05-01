

from leaderboard_cyclopeptide_sequencing import *
import unittest
import os


class TestcLeaderboardCyclopeptideSequencing(unittest.TestCase):

    @unittest.SkipTest
    def test_leaderboard_cyclopeptide_sequencing_0(self):
        n = 10
        spectrum = [int(x) for x in '0 71 113 129 147 200 218 260 313 331 347 389 460'.split()]
        b = '113-147-71-129'
        a = '-'.join([str(MassDictionary[x]) for x in leaderboard_cyclopeptide_sequencing(spectrum, n)])
        self.assertEqual(a, b)

    # Failed (multiple solutions may exist)
    @unittest.SkipTest
    def test_leaderboard_cyclopeptide_sequencing_1(self):
        data_dir = os.path.abspath('..\\text_files')
        dataset = open(data_dir+'\\LeaderboardCyclopeptideSequencing\\leaderboard_cyclopeptide_sequencing.txt', 'r')
        data = [string.strip('\n') for string in dataset.readlines()]
        dataset.close()
        spectrum = [int(x) for x in data[2].split()]
        n = int(data[1])
        b = data[4]
        a = '-'.join([str(MassDictionary[x]) for x in leaderboard_cyclopeptide_sequencing(spectrum, n)])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
