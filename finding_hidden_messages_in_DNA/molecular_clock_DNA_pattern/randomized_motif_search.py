

import random
from profile_matrix_with_pseudocounts import *
from profile_most_probable_kmer import *
from score_motifs import*


def motifs(dna, profile):
    k = len(profile['A'])
    motifs_array = []
    for j in range(len(dna)):
        p = -1
        most_probable = dna[j][0:k]
        for i in range(len(dna[j])-k+1):
            motif_to_compare = dna[j][i:i+k]
            pr = probability(motif_to_compare, profile)
            if pr > p:
                p = pr
                most_probable = motif_to_compare
        motifs_array.append(most_probable)
    return motifs_array


def random_motifs(dna, k, t):
    kmers = []
    for i in range(t):
        r = random.randint(0, len(dna[i])-k)
        kmers.append(dna[i][r:r+k])
    return kmers


def randomized_motif_search(dna, k, t):
    motifs_array = random_motifs(dna, k, t)
    best_motifs = list(motifs_array)
    while True:
        profile = profile_matrix_with_pseudocounts(motifs_array)
        motifs_array = motifs(dna, profile)
        if get_score(motifs_array) < get_score(best_motifs):
            best_motifs = motifs_array
        else:
            return best_motifs


def loop_randomized_motif_search(n, dna, k, t):
    best_motifs = randomized_motif_search(dna, k, t)
    for i in range(n):
        motifs_array = randomized_motif_search(dna, k, t)
        if get_score(best_motifs) > get_score(motifs_array):
            best_motifs = motifs_array
    return best_motifs
