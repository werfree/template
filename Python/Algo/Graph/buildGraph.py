from collections import defaultdict, deque

graph = defaultdict(list)


def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def find_path(graph, start, end, path=[]):
    path.append(start)

    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newPath = find_path(graph, node, end, path)
            if newPath:
                return newPath
            return None


def BFS(graph, s):
    l = len(graph)
    print(l)
    visited = [0] * (l + 2)

    queue = deque()

    queue.append(s)

    visited[s] = 1

    while queue:

        s = queue.popleft()
        print(s)
        for i in graph[s]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


addEdge(graph, 1, 2)
addEdge(graph, 2, 3)
#addEdge(graph, 1, 6)

'''
addEdge(graph, 2, 4)
addEdge(graph, 2, 5)
addEdge(graph, 3, 5)
addEdge(graph, 4, 5)
addEdge(graph, 4, 6)
addEdge(graph, 5, 6)
'''

print(graph)
BFS(graph, 1)
