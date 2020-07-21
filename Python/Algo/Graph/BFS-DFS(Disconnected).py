'''
    For Disconected graph we just need to call all vertexx

'''

from collections import defaultdict, deque


def addEdge(graph, node1, node2):
    graph[node1].append(node2)


def BFS(s):
    visited = set()
    queue = deque()

    for i in graph.copy():
        if i not in visited:
            BFSHELPER(i, visited, queue)


def BFSHELPER(s, visited, queue):
    visited.add(s)
    queue.append(s)

    while queue:
        s = queue.popleft()
        print(s)

        for i in graph[s]:
            if i not in visited:
                visited.add(i)
                queue.append(i)


def DFSHELPER(s, visited):
    visited.add(s)
    print(s, end=" ")

    for i in graph[s]:
        if i not in visited:
            DFSHELPER(i, visited)
    print()


def DFS(s):

    print("in")

    visited = set()
    keys = graph.keys()
    for i in graph.copy():
        if i not in visited:
            DFSHELPER(i, visited)


graph = defaultdict(list)


addEdge(graph, 1, 2)
addEdge(graph, 1, 3)
addEdge(graph, 2, 4)
addEdge(graph, 2, 5)
addEdge(graph, 3, 5)
addEdge(graph, 4, 5)
addEdge(graph, 4, 6)
addEdge(graph, 5, 6)

# Disconnected Edge
addEdge(graph, 7, None)


print(graph)

# Connected Graph
print("BFS")
BFS(1)


print("DFS")
DFS(1)
