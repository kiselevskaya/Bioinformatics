

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
    graph = dict()
    for i in range(len(text)-k+1):
        prefix = text[i:i+k-1]
        suffix = text[i+1:i+k]
        if prefix not in graph.keys():
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph


def de_bruijnk_graph(patterns):
    graph = dict()
    for i in range(len(patterns)):
        prefix = patterns[i][:-1]
        suffix = patterns[i][1:]
        if prefix not in graph.keys():
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph
