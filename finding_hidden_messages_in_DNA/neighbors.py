

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
