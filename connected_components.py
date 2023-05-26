# Q2 connected components
from collections import defaultdict

def connected(graph):
    seen = set()
    comp = 0

    for k,v in graph.items():
        comp += check(graph, k, seen)
    return comp

def check(graph, node, seen):
    if node in seen:
        return 0
    seen.add(node)

    for neigh in graph[node]:
        check(graph, neigh, seen)
    return 1

if __name__=="__main__":
    edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
    ['a','b']
    ]

    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    print(connected(graph))