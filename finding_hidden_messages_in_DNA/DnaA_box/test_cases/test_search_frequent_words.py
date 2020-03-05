

from search_frequent_words import *
import unittest


class TestSearchFrequentWords(unittest.TestCase):

    @unittest.SkipTest
    def test_frequent_words_with_mismatches_0(self):
        text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
        k, d = 4, 1
        a = ' '.join(frequent_words_with_mismatches(text, k, d))
        b = 'GATG ATGC ATGT'
        self.assertCountEqual(a, b)

    @unittest.SkipTest
    def test_frequent_words_with_mismatches_1(self):
        text = 'AATCCTCCGGGCGGGTATCTGCCGGGCTGCCGGGCCTCCTGCTATCGGGCTGCCGGGTATTATTATAATTATTATCGGGTATCCTCCTGCAATCTGCTATCCTCCCTCCTGCCTGCTATCGGGTATTATTATAATCTGCCCTCAATCCTCAATCTGCTATCTGCTATCTGCCCTCCCTCCTGCCGGGCGGGAATTATCGGGCGGGCGGGTATCCTCCTGCCGGGCGGGCTGCCTGCTATCTGCAATCTGCCTGCCGGGCGGGTATCTGCCTGCAATCGGGCTGCCCTCCTGCCCTCCCTCAATCCTCTATCTGCCCTCCCTC'
        k, d = 5, 3
        a = ' '.join(frequent_words_with_mismatches(text, k, d))
        b = 'CGCCG'
        self.assertCountEqual(a, b)

    def test_frequent_words_with_mismatches_and_reverse_0(self):
        text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
        k, d = 4, 1
        mismatch_and_reverse = frequent_words_with_mismatches_and_reverse(text, k, d)
        a = ' '.join(mismatch_and_reverse)
        b = 'ATGT ACAT'
        self.assertCountEqual(a, b)

    def test_frequent_words_with_mismatches_and_reverse_1(self):
        text = 'CGGAACGGAAGAACGCGCGCGGACGTCGTCGTCGCGTGAACGCGTCGGACGGACGGAACGGACGTCGCGTCGGACGGAGAACGCGGAACGGAGACGCGGAGAACGCGGAAGAACGCGTCGGAACGCGGAGAAGAGAACGGAGACGTGAAGACGTCGCGGACGCGCGCGCGCGGAACGGAGAACGGACGCGGACGTCGCGCGGAAGAACGCGTCGCGCGGAGAGAA'
        k, d = 6, 3
        mismatch_and_reverse = frequent_words_with_mismatches_and_reverse(text, k, d)
        a = ' '.join(mismatch_and_reverse)
        b = 'CGCCCG CGGGCG'
        self.assertCountEqual(a, b)

    def test_frequent_words_with_mismatches_sorting_0(self):
        text = 'AATCCTCCGGGCGGGTATCTGCCGGGCTGCCGGGCCTCCTGCTATCGGGCTGCCGGGTATTATTATAATTATTATCGGGTATCCTCCTGCAATCTGCTATCCTCCCTCCTGCCTGCTATCGGGTATTATTATAATCTGCCCTCAATCCTCAATCTGCTATCTGCTATCTGCCCTCCCTCCTGCCGGGCGGGAATTATCGGGCGGGCGGGTATCCTCCTGCCGGGCGGGCTGCCTGCTATCTGCAATCTGCCTGCCGGGCGGGTATCTGCCTGCAATCGGGCTGCCCTCCTGCCCTCCCTCAATCCTCTATCTGCCCTCCCTC'
        k, d = 5, 3
        a = ' '.join(list(frequent_words_with_mismatches_sorting(text, k, d)))
        b = 'CGCCG'
        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
