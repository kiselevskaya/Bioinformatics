

from score_motifs import *
from profile_most_probable_kmer import *


def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][0:k])
    n = len(dna[0])
    for e in range(n-k+1):
        motifs = []
        motifs.append(dna[0][e:e+k])
        for j in range(1, t):
            profile = profile_matrix(motifs)
            most_probable = profile_most_probable_kmer(dna[j], k, profile)
            motifs.append(most_probable)
        if get_score(motifs) < get_score(best_motifs):
            best_motifs = motifs
    return best_motifs
