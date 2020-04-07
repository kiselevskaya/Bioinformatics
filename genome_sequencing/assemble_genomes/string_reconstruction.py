

from composition import *
from eulerian_path import *


def string_reconstruction(patterns):
    graph = de_bruijnk_graph(patterns)
    path = eulerian_path(graph)
    genome = path_to_genome(path)
    return genome
