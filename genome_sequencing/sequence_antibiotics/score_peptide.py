

from cyclospectrum import *


def score_peptide(peptide, spectrum):
    score = 0
    cyclo_spectrum = cyclospectrum(peptide)
    unique = list(set(cyclo_spectrum))
    for i in range(len(unique)):
        score += min([cyclo_spectrum.count(unique[i]), spectrum.count(unique[i])])
    return score
