

import timeit
from hamming_distance import *


def immediate_neighbors(pattern):
    neighborhood = set()
    for i in range(len(pattern)):
        symbol = pattern[i]
        for x in "ACTG":
            if x != symbol:
                neighbor = pattern[:i] + x + pattern[i+1:]
                neighborhood.add(neighbor)
    return neighborhood


def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for suffix in suffix_neighbors:
        if hamming_distance(pattern[1:], suffix) < d:
            for nucleotide in {'A', 'C', 'G', 'T'}:
                neighborhood.add(nucleotide+suffix)
        else:
            neighborhood.add(pattern[:1]+suffix)
    return neighborhood


def frequent_words_with_mismatches_sorting(text, k, d):
    frequent_patterns = set()
    neighborhoods = []
    indexes = []
    for i in range(len(text) - k + 1):
        neighborhoods += (list(neighbors(text[i:i+k], d)))
    for j in range(len(neighborhoods)):
        indexes.append(pattern_to_number(neighborhoods[j]))
    count = [1] * len(indexes)
    sorted_index = sorted(indexes)
    for n in range(len(neighborhoods) - 1):
        if sorted_index[n] == sorted_index[n + 1]:
            count[n + 1] = count[n] + 1
    max_count = max(count)
    for m in range(len(neighborhoods)):
        if count[m] == max_count:
            pattern = number_to_pattern(sorted_index[m], k)
            frequent_patterns.add(pattern)
    return frequent_patterns


start = timeit.default_timer()

text = 'AATCCTCCGGGCGGGTATCTGCCGGGCTGCCGGGCCTCCTGCTATCGGGCTGCCGGGTATTATTATAATTATTATCGGGTATCCTCCTGCAATCTGCTATCCTCCCTCCTGCCTGCTATCGGGTATTATTATAATCTGCCCTCAATCCTCAATCTGCTATCTGCTATCTGCCCTCCCTCCTGCCGGGCGGGAATTATCGGGCGGGCGGGTATCCTCCTGCCGGGCGGGCTGCCTGCTATCTGCAATCTGCCTGCCGGGCGGGTATCTGCCTGCAATCGGGCTGCCCTCCTGCCCTCCCTCAATCCTCTATCTGCCCTCCCTC'
k, d = 5, 3
print(frequent_words_with_mismatches_sorting(text, k, d))   # {'CGCCG'}

stop = timeit.default_timer()
print("Program Executed in", stop-start)


