

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
    # print('Graph: ', graph)
    path = eulerian_path(graph)
    # print('Path: ', path)
    path = [path[i].split('|') for i in range(len(path))]
    start = ''.join([path[i][0][0] for i in range(len(path)-1)])+path[-1][0]
    end = (''.join([path[i][1][0] for i in range(len(path)-1)])+path[-1][1])[-(k+d):]
    genome = start+end
    return genome


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath('..\\assemble_genomes\\text_files')
    dataset = open(data_dir+'\\PairedStringReconstruction\\inputs\\dataset_204_16.txt', 'r')
    input = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    k, d = int(input[0].split()[0]), int(input[0].split()[1])
    pairs = [x.split('|') for x in input[1:]]

    data = open(data_dir+'\\PairedStringReconstruction\\outputs\\dataset_204_16.txt', 'r')
    output = [string.strip('\n') for string in data.readlines()]
    data.close()

    a = paired_path_to_genome(pairs, k, d)

    print(a)


