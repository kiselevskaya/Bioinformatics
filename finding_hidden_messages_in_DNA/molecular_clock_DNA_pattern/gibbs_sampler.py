

from randomized_motif_search import *
from profile_matrix_with_pseudocounts import *


def normalize(probabilities):
    total = sum(probabilities.values())
    normalized = {k: probabilities[k] / total for k in probabilities}
    return normalized


def weighted_die(probabilities):
    r = random.uniform(0, 1)
    for key in probabilities:
        r -= probabilities[key]
        if r <= 0:
            return key


def profile_generated_string(text, profile, k):
    n = len(text)
    probabilities = {}
    for i in range(0, n-k+1):
        probabilities[text[i:i+k]] = probability(text[i:i+k], profile)
    probabilities = normalize(probabilities)
    return weighted_die(probabilities)


def gibbs_sampler(dna, k, t, n):
    # motifs_array = randomized_motif_search(dna, k, t)
    motifs_array = loop_randomized_motif_search(100, dna, k, t)
    best_motifs = list(motifs_array)
    for j in range(n):
        i = random.randint(0, t-1)
        excluded = [x for x in motifs_array if motifs_array.index(x) != i]
        profile = profile_matrix_with_pseudocounts(excluded)
        motifs_array[i] = profile_generated_string(dna[i], profile, k)
        if get_score(motifs_array) < get_score(best_motifs):
            best_motifs = motifs_array
    return best_motifs
