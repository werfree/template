from collections import defaultdict, deque

graph = defaultdict(list)


def addEdge(graph, u, v):
    graph[u].append(v)


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


def BFS(graph, s, d):
    l = len(graph)
    print(l)
    visited = defaultdict(int)

    queue = deque()

    queue.append(s)

    visited[s] = 0

    while queue:

        s = queue.popleft()
        if s == d:
            print(visited[s])
            break
        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited[i] = 1 + visited[s]


addEdge(graph, 1, 2)
addEdge(graph, 1, 3)
addEdge(graph, 2, 4)
addEdge(graph, 2, 5)
addEdge(graph, 3, 5)
addEdge(graph, 4, 5)
addEdge(graph, 4, 6)
addEdge(graph, 5, 6)


print(graph)
BFS(graph, 1, 2)
