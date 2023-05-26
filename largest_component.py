#largest component

from collections import defaultdict



def largest(graph):
    seen = set()
    largest = 0
    
    for k,v in graph.items():
        size = check(graph, k, seen)
        largest = max(largest, size)
    return largest

def check(graph, node, seen):
    if node in seen:
        return 0
    count = 1
    seen.add(node)
    for neigh in graph[node]:
        count += check(graph, neigh, seen)
    return count

if __name__=="__main__":
    edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
    ['a','b'],
    ['b','c'],
    ['c','d'],
    ['d','e'],
    ['e','f']
    ]

    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    print(largest(graph))