
from computing_frequencies import *
from pattern_to_number_and_back import *


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count


def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern in freq.keys():
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    return freq


def frequent_words(text, k):
    words = []
    freq = frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words


def faster_frequent_words(text, k):
    frequent_patterns = []
    frequency_array = computing_frequencies(text, k)
    max_count = max(frequency_array)
    for i in range(4**k):
        if frequency_array[i] == max_count:
            number = i
            pattern = number_to_pattern(number, k)
            frequent_patterns.append(pattern)
    return frequent_patterns


def frequent_words_by_sorting(text, k):
    frequent_patterns = []
    index_array = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        index_array.append(pattern_to_number(pattern))
    index_array = sorted(index_array)
    count_patterns = [1]+[0]*(len(index_array)-1)
    for i in range(1, len(text)-k+1):
        if index_array[i] == index_array[i-1]:
            count_patterns[i] = count_patterns[i-1]+1
        else:
            count_patterns[i] = 1
    max_count = max(count_patterns)
    for i in range(len(count_patterns)):
        if count_patterns[i] == max_count:
            pattern = number_to_pattern(index_array[i], k)
            frequent_patterns.append(pattern)
    return frequent_patterns
