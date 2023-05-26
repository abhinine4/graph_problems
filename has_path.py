# Q1 find path (src - dst)
# check f -> k

#dfs
def haspath_dfs(graph, src, dst):
    if src == dst:
        return True
    if src not in graph:
        return False
    for node in graph[src]:
        if haspath_dfs(graph, node, dst) == True:
            return True
    return False


#bfs
def haspath_bfs(graph, src, dst):
    q = [src]

    while q:
        node = q.pop()
        if node == dst:
            return True
        for neigh in graph[node]:
            q.append(neigh)
    return False



if __name__== "__main__":
    graph = {
    'f' : ['g','i'],
    'g' : ['h'],
    'h' : [],
    'i' : ['g','k'],
    'j' : ['i'],
    'k' : []
    } 
    
    print(haspath_bfs(graph, 'k', 'c'))
    # haspath_dfs(graph, 'f', 'k')
