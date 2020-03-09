

from neighbors import *


def motif_enumeration(dna, k, d):
    neighbors_arrays = []
    for i in range(len(dna)):
        kmers = []
        for j in range(len(dna[0])-k+1):
            kmers.append(dna[i][j:j+k])
        neighbor = []
        for m in range(len(kmers)):
            neighbor.extend(list(neighbors(kmers[m], d)))
        neighbors_arrays.append(list(set(neighbor)))
    motifs = set.intersection(*map(set, neighbors_arrays))
    return motifs
