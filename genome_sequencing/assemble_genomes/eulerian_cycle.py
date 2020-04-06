
import random


def eulerian_cycle(graph):
    print(graph)
    cycle = []
    stack = []
    location = None
    # if [k for k, v in graph.items() if len(v) % 2 == 0] == list(graph.keys()):
    #     location = random.choice(list(graph.keys()))
    # elif len([k for k, v in graph.items() if len(v) % 2 == 0]) == 2:
    #     location = random.choice([k for k, v in graph.items() if len(v) % 2 == 0])
    # else:
    #     print('Eulerian path doesn\'t exist')

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


import os
data_dir = os.path.abspath('..\\assemble_genomes\\text_files')
dataset = open(data_dir+'\\EulerianCycle\\inputs\\dataset_203_2.txt', 'r')
input = [string.strip('\n') for string in dataset.readlines()]
dataset.close()
graph = dict((y[0], y[2:]) for y in (x.replace(',', ' ').split() for x in input))

print('->'.join(eulerian_cycle(graph)))
