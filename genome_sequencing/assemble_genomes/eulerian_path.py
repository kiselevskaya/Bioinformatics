

import random


def eulerian_path(graph):
    path = []
    stack = []
    indegree = sum(list(graph.values()), [])
    outdegree = list(graph.keys())
    start = [x for x in outdegree if (x not in indegree) or len(graph[x]) > indegree.count(x)]

    if not start:
        location = random.choice(outdegree)
    elif len(start) == 1:
        location = start[0]
    else:
        location = random.choice(start)
    start = location

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
            path.append(location)
            location = stack[-1]
            stack.pop()
            if not stack and not graph:
                path.append(location)

    if path[0] != start:
        path = path[::-1]

    return path
