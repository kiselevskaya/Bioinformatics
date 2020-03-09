

from hamming_distance import *
from pattern_to_number_and_back import *


def median_sorting(dna, k):
    distance = k*len(dna)
    kmers = []
    median = ''
    for i in range(4**k):
        kmers.append(number_to_pattern(i, k))
    for kmer in kmers:
        for i in range(len(dna)):
            for j in range(len(dna[i])-k+1):
                if distance > hamming_distance(kmer, dna[i][j:j+k]):
                    distance = hamming_distance(kmer, dna[i][j:j+k])
                    median = kmer

    return median
