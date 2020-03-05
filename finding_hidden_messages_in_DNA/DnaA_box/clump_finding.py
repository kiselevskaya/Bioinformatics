

from pattern_count import frequency_map
from pattern_matching import *


def clump_finding(genome, k, l, t):
    freq_map = frequency_map(genome, k)
    words = []
    for key in freq_map:
        if freq_map[key] >= t:
            words.append(key)
    output = []
    for pattern in words:
        match = pattern_matching(pattern, genome)
        for i in range(len(match)):
            try:
                last_index_l = i+t-1
                if match[last_index_l]+k-1 <= match[i]+l-1:
                    output.append(pattern)
                    break
            except Exception as e:
                break
    return output


def clump_finding_efficient(genome, k, l, t):
    freq = {}
    n = len(genome)
    for i in range(n-k+1):
        pattern = genome[i:i+k]
        if pattern in freq.keys():
            freq[pattern].append(i)
        else:
            freq[pattern] = [i]
    patterns = []
    for key in freq:
        if len(freq[key]) >= t:
            for j in range(len(freq[key])):
                try:
                    last_index_l = j+t-1
                    if freq[key][last_index_l]+k-1 <= freq[key][j]+l-1:
                        patterns.append(key)
                        break
                except Exception as e:
                    break
    return patterns
