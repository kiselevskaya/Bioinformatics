

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

    return '->'.join(path)


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath('..\\assemble_genomes\\text_files')
    dataset = open(data_dir+'\\EulerianPath\\inputs\\sample.txt', 'r')
    input = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    data = open(data_dir+'\\EulerianPath\\outputs\\sample.txt', 'r')
    output = [string.strip('\n') for string in data.readlines()]
    data.close()
    print(output)
    print()

    graph = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in input))
    path = eulerian_path(graph)
    print(path)
