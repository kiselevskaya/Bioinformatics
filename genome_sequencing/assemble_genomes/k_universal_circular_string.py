

from composition import *
from eulerian_cycle import *


def k_universal_circular_string(k):
    patterns = ['{:0{}b}'.format(i, k) for i in range(2**k)]
    graph = de_bruijnk_graph(patterns)
    cycle = eulerian_cycle(graph)
    genome = path_to_genome(cycle)
    return genome[(k-1):]
