

def probability(motif, profile):
    probable = 1
    for i in range(len(motif)):
        char = motif[i]
        probable *= profile[char][i]
    return probable


def profile_most_probable_kmer(text, k, profile):
    p = -1
    most_probable = text[0:k]
    for i in range(len(text)-k+1):
        motif_to_compare = text[i:i+k]
        pr = probability(motif_to_compare, profile)
        if pr > p:
            p = pr
            most_probable = motif_to_compare
    return most_probable
