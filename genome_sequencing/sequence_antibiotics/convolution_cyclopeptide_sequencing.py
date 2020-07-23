

from spectral_convolution import *
from extended_leaderboard_peptide_sequencing import *


def extended_alphabet(m, spectrum):
    convolution = spectral_convolution(spectrum)
    unique = list(set(convolution))
    frequency = dict((x, convolution.count(x)) for x in unique if 200 >= x >= 57)
    trim = sorted(frequency.items(), key=lambda item: item[1])[-m][1]
    frequency = [k for k, v in frequency.items() if v >= trim]
    alphabet = dict((str(chr(i)), i) for i in frequency)
    return alphabet


def convolution_cyclopeptide_sequencing(m, n, spectrum):
    alphabet = extended_alphabet(m, spectrum)

    leaderboard = extended_leaderboard_peptide_sequencing(spectrum, n, alphabet)
    leader_peptide = leaderboard[0][0]
    n_leaders = leaderboard[1]
    return [leader_peptide, n_leaders, alphabet]


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()

    import os
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\ConvolutionCyclopeptideSequencing\\dataset_104_8.txt', 'r')
    data = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    m = int(data[0])
    n = int(data[1])
    spectrum = sorted([int(x) for x in data[2].split()])

    a = convolution_cyclopeptide_sequencing(m, n, spectrum)
    # print('-'.join([str(a[1][x]) for x in a[0]]))
    alphabet = a[2]
    m = max([v[1] for v in a[1].values()])
    c = {k: v for k, v in a[1].items() if v[1] == m}
    print('\n', 'score:', m, 'matches:', len(c), '\n')
    for k in c.keys():
        print('-'.join([str(alphabet[x]) for x in k]))

    stop = timeit.default_timer()
    print('\n', "Program Executed in", stop-start)
