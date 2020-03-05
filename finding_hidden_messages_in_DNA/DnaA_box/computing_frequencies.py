

from pattern_to_number_and_back import *


def computing_frequencies(text, k):
    frequency_array = [0]*(4**k)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array
