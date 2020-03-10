

from hamming_distance import *
from pattern_to_number_and_back import *


def median_sorting(dna, k):
    distance = k*len(dna)
    kmers = []
    median = ''
    for i in range(4**k):
        kmers.append(number_to_pattern(i, k))
    for kmer in kmers:
        new_distance = sum([min([hamming_distance(string[i:i+k], kmer) for i in range(len(string) - k + 1)]) for string in dna])
        if distance > new_distance:
            distance = new_distance
            median = kmer
    return median
