
from pattern_to_number_and_back import *
from reverse_complement import *
from neighbors import *
from hamming_distance import *


def frequent_words_with_mismatches(text, k, d):
    words = []
    all = {}
    for i in range(4**k):
        pattern = number_to_pattern(i, k)
        all[number_to_pattern(i, k)] = approximate_pattern_count(text, pattern, d)
    max_freq = max(all.values())
    for key, value in all.items():
        if value == max_freq:
            words.append(key)
    return words


def frequent_words_with_mismatches_and_reverse(text, k, d):
    words = []
    all = {}
    for i in range(4**k):
        pattern = number_to_pattern(i, k)
        reverse_pattern = reverse_complement(pattern)
        count = approximate_pattern_count(text, pattern, d)
        reverse_count = approximate_pattern_count(text, reverse_pattern, d)
        all[number_to_pattern(i, k)] = count + reverse_count
    max_freq = max(all.values())
    for key, value in all.items():
        if value == max_freq:
            words.append(key)
    return words


def frequent_words_with_mismatches_sorting(text, k, d):
    frequent_patterns = set()
    neighborhoods = []
    indexes = []
    for i in range(len(text) - k + 1):
        # neighborhoods += (list(neighbors(text[i:i+k], d)))
        neighborhoods += (list(neighbors(text[i:i+k], d)))+(list(neighbors(reverse_complement(text[i:i+k]), d)))
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
