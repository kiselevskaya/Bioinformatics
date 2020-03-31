

def composition(text, k):
    lst = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        lst.append(kmer)
    return sorted(lst)


def path_to_genome(path):
    genome = ''
    for i in range(len(path)):
        if i == 0:
            genome += path[i]
        else:
            genome += path[i][-1]
    return genome
