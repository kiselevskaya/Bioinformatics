

def composition(text, k):
    lst = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        lst.append(kmer)
    # return sorted(lst)
    return lst


def path_to_genome(path):
    genome = ''
    for i in range(len(path)):
        if i == 0:
            genome += path[i]
        else:
            genome += path[i][-1]
    return genome


def overlap(patterns):
    edges = {}
    for i in range(len(patterns)):
        suffix = patterns[i][1:]
        for j in range(len(patterns)):
            if j == i:
                continue
            else:
                prefix = patterns[j][:-1]
            if suffix == prefix:
                if patterns[i] not in edges:
                    edges[patterns[i]] = [patterns[j]]
                else:
                    edges[patterns[i]].append(patterns[j])
    return edges


def de_bruijnk(text, k):
    edges = composition(text, k-1)
    edges = dict((kmer, []) for kmer in sorted(set(edges)))
    patterns = composition(text, k)
    for i in range(len(patterns)):
        prefix = patterns[i][:-1]
        suffix = patterns[i][1:]
        for j in range(len(edges.keys())):
            edge = list(edges.keys())[j]
            if prefix == edge:
                edges[edge].append(suffix)
    edges = {i: edges[i] for i in edges if edges[i] != []}
    return edges
