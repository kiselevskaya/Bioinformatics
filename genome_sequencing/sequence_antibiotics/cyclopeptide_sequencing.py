

from cyclospectrum import *
from linear_spectrum import *


MassDictionary = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def expansion(candidate_peptides, aminoAcids):
    n = len(candidate_peptides)
    for i in range(len(candidate_peptides)):
        for j in range(len(aminoAcids)):
            candidate_peptides.append(candidate_peptides[i]+aminoAcids[j])
    candidate_peptides = list(candidate_peptides[n:])
    return candidate_peptides


def cyclopeptide_sequencing(spectrum):
    candidate_peptides = ['']
    collection = []
    aminoAcids = [x for x in list(MassDictionary.keys()) if MassDictionary[x] in spectrum]
    while candidate_peptides:
        candidate_peptides = expansion(candidate_peptides, aminoAcids)
        good_peptide = []
        for p in candidate_peptides:
            mass = sum([MassDictionary[p[i]] for i in range(len(p))])
            if mass == spectrum[-1]:
                if cyclospectrum(p) == spectrum and p not in collection:
                    collection.append(p)
            elif all(x in spectrum for x in linear_spectrum(p)) and p != '':
                good_peptide.append(p)
        candidate_peptides = good_peptide
    return collection


def peptides_collection_as_amino_masses(collection):
    all_combinations = [[str(MassDictionary[x]) for x in peptide] for peptide in collection]
    unique_combinations = ' '.join(list(set(['-'.join(x) for x in all_combinations])))
    return unique_combinations
