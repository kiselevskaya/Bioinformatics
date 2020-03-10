

from hamming_distance import *


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    # return sum([min([hamming_distance(string[i:i+k], pattern) for i in range(len(string) - k + 1)]) for string in dna])
    distance = 0
    for i in range(len(dna)):
        hamming_dist = k*len(dna)
        for j in range(len(dna[i])-k+1):
            if hamming_dist > hamming_distance(pattern, dna[i][j:j+k]):
                hamming_dist = hamming_distance(pattern, dna[i][j:j+k])
        distance += hamming_dist
    return distance
