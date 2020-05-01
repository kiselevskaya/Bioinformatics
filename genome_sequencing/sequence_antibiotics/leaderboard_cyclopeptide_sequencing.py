

from linear_spectrum import *
from score_peptide import *


MassDictionary = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def linear_peptide_score(peptide, spectrum):
    score = 0
    linear = linear_spectrum(peptide)
    unique = list(set(linear))
    for i in range(len(unique)):
        score += min([linear.count(unique[i]), spectrum.count(unique[i])])
    return score


def leaderboard_cyclopeptide_sequencing(spectrum, n):
    leaderboard = {'': [0, 1]}
    leader_peptide = ['', 0, 1]
    while leaderboard:
        extract = dict(leaderboard)
        leaderboard = {}
        for k, v in extract.items():
            for key, value in MassDictionary.items():
                peptide = k+key
                mass = v[0]+value
                if mass <= spectrum[-1]:
                    score = linear_peptide_score(peptide, spectrum)
                    leaderboard[peptide] = [mass, score]
                    if mass == spectrum[-1]:
                        if score > leader_peptide[2]:
                            leader_peptide = [peptide, mass, score]
        try:
            trim = sorted(leaderboard.items(), key=lambda item: item[1][1])[-n][1][1]
            leaderboard = {k: v for k, v in leaderboard.items() if v[1] >= trim}
        except IndexError:
            continue
    return leader_peptide[0]
