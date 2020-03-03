

def reverse_complement(pattern):
    complement = ''
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in range(len(pattern)):
        complement += complements[pattern[i]]
    return complement[::-1]
