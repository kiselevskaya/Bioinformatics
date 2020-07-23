

from linear_spectrum import *
from score_peptide import *


Alphabet = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113: 'I/L', 114: 'N', 115: 'D', 128: 'K/Q', 129: 'E', 131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}


def linear_peptide_score(peptide, spectrum):
    score = 0
    linear = linear_spectrum(peptide)
    unique = list(set(linear))
    for i in range(len(unique)):
        score += min([linear.count(unique[i]), spectrum.count(unique[i])])
    return score


def n_leaderboard_peptides_sequencing(spectrum, n):
    leaderboard = {'': [0, 1]}
    leader_peptide = ['', 0, 1]
    thirty_eight = {}
    while leaderboard:
        extract = dict(leaderboard)
        leaderboard = {}
        for k, v in extract.items():
            for key, value in Alphabet.items():
                peptide = k+value.split('/')[0]
                mass = v[0]+key
                if mass <= spectrum[-1]:
                    score = linear_peptide_score(peptide, spectrum)
                    leaderboard[peptide] = [mass, score]
                    if mass == spectrum[-1]:
                        cycloscore = score_peptide(peptide, spectrum)
                        thirty_eight[peptide] = [mass, cycloscore]
                        if cycloscore > leader_peptide[2]:
                            leader_peptide = [peptide, mass, cycloscore]
        try:
            trim = sorted(leaderboard.items(), key=lambda item: item[1][1])[-n][1][1]
            leaderboard = {k: v for k, v in leaderboard.items() if v[1] >= trim}
        except IndexError:
            continue
    return thirty_eight


if __name__ == '__main__':
    import timeit
    import os
    start = timeit.default_timer()
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\LeaderboardCyclopeptideSequencing\\dataset_102_10.txt', 'r')
    data = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    n = int(data[0])
    spectrum = [int(x) for x in data[1].split()]

    a = n_leaderboard_peptides_sequencing(spectrum, n)

    m = max([v[1] for v in a.values()])
    c = {k: v for k, v in a.items() if v[1] == m}
    print('\n', 'score:', m, 'matches:', len(c), '\n')
    for k in c.keys():
        print('-'.join([str(MassDictionary[x]) for x in k]))

    stop = timeit.default_timer()
    print("Program Executed in", stop-start)

