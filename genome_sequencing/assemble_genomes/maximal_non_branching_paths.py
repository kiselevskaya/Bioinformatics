

from string_reconstruction import *
from eulerian_cycle import *


def maximal_non_branching_paths(graph):
    numbers = False
    indegree = sum(list(graph.values()), [])
    pathes = []
    for key, value in graph.items():
        if indegree.count(key) != 1 or len(value) != 1:
            for val in value:
                try:
                    non_branched_path = [key, str(int(val))]
                    numbers = True
                except Exception as e:
                    non_branched_path = key+val[-1]
                while val in graph.keys() and indegree.count(val) == 1 and len(graph[val]) == 1 and graph[val][0] != non_branched_path[1]:
                    try:
                        non_branched_path.append(str(int(graph[val][0])))
                    except Exception as e:
                        non_branched_path += graph[val][0][-1]
                    val = graph[val][0]
                if numbers:
                    non_branched_path = ' -> '.join(non_branched_path)
                pathes.append(non_branched_path)

    one_to_one = dict((key, value) for key, value in graph.items() if (indegree.count(key) == 1 and len(value) == 1 and indegree.count(value[0]) == 1))
    cycles = []
    while one_to_one:
        for k, v in one_to_one.items():
            cycle = {}
            cycle[k] = v
            val = v[0]
            while val in one_to_one.keys() and val not in cycle.keys():
                cycle[val] = one_to_one[val]
                val = one_to_one[val][0]
            if val in cycle.keys():
                one_to_one = {k: v for k, v in one_to_one.items() if k not in cycle or v != cycle[k]}
                cycles.append(eulerian_cycle(cycle))
            else:
                one_to_one = {k: v for k, v in one_to_one.items() if k not in cycle or v != cycle[k]}
            break

    if numbers:
        cycles = [' -> '.join(x) for x in cycles]
    else:
        cycles = [string_reconstruction(cycle) for cycle in cycles]
    pathes.extend(cycles)

    return pathes
