

from collections import defaultdict, deque
import heapq


class Graph():

    def __init__(self, v):
        self.V = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((w, v))
        self.graph[v].append((w, u))

    def prims(self, s):
        graph = self.graph
        V = self.V
        visited = set()
        key = [float("inf")] * V
        pre = [None] * V
        key[s] = 0

        q = [(0, s)]
        i = 0
        while q:
            weight, s = heapq.heappop(q)

            if s in visited:
                continue
            visited.add(s)
            for curWeight, v in graph[s]:
                if v in visited:
                    continue
                if curWeight <= key[v]:
                    key[v] = curWeight
                    pre[v] = s
                    heapq.heappush(q, (curWeight, v))

        print(sum(key[1:]))
        print(pre)


graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
print(graph.prims(0))
