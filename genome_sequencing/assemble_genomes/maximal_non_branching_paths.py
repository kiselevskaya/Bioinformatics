

from string_reconstruction import *
from eulerian_cycle import *


def maximal_non_branching_paths(graph):
    indegree = sum(list(graph.values()), [])
    pathes = []
    for key, value in graph.items():
        if indegree.count(key) != 1 or len(value) != 1:
            for val in value:
                non_branched_path = key+val[-1]
                while val in graph.keys() and indegree.count(val) == 1 and len(graph[val]) == 1:
                    non_branched_path += graph[val][0][-1]
                    val = graph[val][0]
                pathes.append(non_branched_path)
    cycle = dict((key, value) for key, value in graph.items() if (indegree.count(key) == 1 and len(value) == 1 and indegree.count(value[0]) == 1))
    if len(cycle.keys()) > 1:
        try:
            cycle = eulerian_cycle(cycle)
            pathes.append(string_reconstruction(cycle))
        except Exception as e:
            print(e)
    return pathes
