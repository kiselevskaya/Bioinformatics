

import math


def get_count(motifs):
    count = {}
    k = len(motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    return count


def get_score(motifs):
    consensus = list(get_consensus(motifs))
    mismatches = 0
    for motif in motifs:
        mismatches += sum(1 for i, j in zip(motif, consensus) if i != j)
    return mismatches


def profile_matrix(motifs):
    t = len(motifs)
    profile = get_count(motifs)
    for key in profile:
        profile[key] = [float(round(counts/t, 1)) for counts in profile[key]]
    return profile


def get_consensus(motifs):
    k = len(motifs[0])
    count = get_count(motifs)
    consensus = ''
    for j in range(k):
        m = 0
        frequent_symbol = ''
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequent_symbol = symbol
        consensus += frequent_symbol
    return consensus


def get_entropy(profile):
    entropy = 0
    for key in profile:
        for fl in profile[key]:
            if fl != 0:
                entropy += fl*math.log2(fl)
    return -entropy
