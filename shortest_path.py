# shortest path (based on number of edges) w -> z
from collections import defaultdict


def shortest(graph, start, end):
    seen = set([start])
    queue = [[start,0]]

    while queue:
        node, distance = queue.pop()
        if node == end:
            return distance
        for neigh in graph[node]:
            if neigh not in seen:
                seen.add(neigh)
                queue.append([neigh, distance+1])
    return -1

if __name__=="__main__":
    edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v'],
    ['a','b'],
    ['b','c'],
    ['c','w'],
    ['w','x']
    ]

    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    print(shortest(graph, 'w', 'y'))    