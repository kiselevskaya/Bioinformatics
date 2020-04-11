

from eulerian_path import *


def de_bruijnk_graph_pairs(pairs):
    graph = dict()
    for i in range(len(pairs)):
        prefix = '|'.join([pairs[i][0][:-1], pairs[i][1][:-1]])
        suffix = '|'.join([pairs[i][0][1:], pairs[i][1][1:]])
        if prefix not in graph.keys():
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph


def paired_path_to_genome(pairs, k, d):
    graph = de_bruijnk_graph_pairs(pairs)
    path = eulerian_path(graph)
    path = [path[i].split('|') for i in range(len(path))]
    start = ''.join([path[i][0][0] for i in range(len(path)-1)])+path[-1][0]
    end = (''.join([path[i][1][0] for i in range(len(path)-1)])+path[-1][1])[-(k+d):]
    genome = start+end
    return genome
