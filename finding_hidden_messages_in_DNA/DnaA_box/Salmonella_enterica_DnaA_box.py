

import os
from skew_array import *
from search_frequent_words import *
import timeit


start = timeit.default_timer()

salmonella = open(os.getcwd()+'\\text_files\\Salmonella_enterica.txt', 'r')
genome = ''.join(salmonella.readlines()).replace('\n', '')
salmonella.close()


def salmonella_enterica_dnaa_box(genome, k, d):
    dnaA_box = ''
    frequency = {}
    minimum = minimum_skew(genome)
    print('Minimum skew at position(s):', minimum)
    check_boxes = [[minimum[0], minimum[0]+500],
                   [minimum[-1]-500, minimum[-1]],
                   [sum(minimum)//len(minimum)-250, sum(minimum)//len(minimum)+250]]
    for l in range(len(check_boxes)):
        text = genome[check_boxes[l][0]:check_boxes[l][1]]
        frequent_words = frequent_words_with_mismatches_sorting(text, k, d)
        count = len(frequent_words)
        frequency[str(check_boxes[l])] = count
    for key, value in frequency.items():
        if value == max(frequency.values()):
            dnaA_box = key
    return dnaA_box


print(salmonella_enterica_dnaa_box(genome, 9, 1))


stop = timeit.default_timer()
print("Program Executed in", stop-start)
