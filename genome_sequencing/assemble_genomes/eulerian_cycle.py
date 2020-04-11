

import random


def eulerian_cycle(graph):
    cycle = []
    stack = []
    location = random.choice(list(graph.keys()))
    while graph or stack:
        try:
            if len(graph[location]) == 1:
                stack.append(location)
                location = graph[location][0]
                del graph[stack[-1]]
            elif len(graph[location]) > 1:
                stack.append(location)
                location = random.choice(graph[location])
                graph[stack[-1]].remove(location)
        except Exception as e:
            cycle.append(location)
            location = stack[-1]
            stack.pop()
            if not stack:
                cycle.append(location)
    return cycle[::-1]
