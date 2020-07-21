

from collections import defaultdict
import heapq


class Graph():
    def __init__(self,):

        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((w, v))

    def dijktraWeight(self, s):
        visited = set()
        d = [float("inf")] * len(self.graph)
        d[s] = 0
        pQueue = []
        heapq.heappush(pQueue, (0, s))

        while pQueue:
            sWeight, s = heapq.heappop(pQueue)
            visited.add(s)
            if d[s] < sWeight:
                continue
            for curWeight, v in self.graph[s]:
                if v in visited:
                    continue
                newDistance = sWeight + curWeight
                if newDistance < d[v]:
                    d[v] = newDistance
                    heapq.heappush(pQueue, (newDistance, v))
        return d

    def dijktraPath(self, s):
        visited = set()
        prev = [None] * (len(self.graph))
        d = [float("inf")] * (len(self.graph) + 6)
        d[s] = 0
        pQueue = []
        heapq.heappush(pQueue, (0, s))

        while pQueue:
            sWeight, s = heapq.heappop(pQueue)
            visited.add(s)
            if d[s] < sWeight:
                continue
            for curWeight, v in self.graph[s]:
                if v in visited:
                    continue
                newDistance = sWeight + curWeight
                if newDistance < d[v]:
                    d[v] = newDistance
                    prev[v] = s
                    heapq.heappush(pQueue, (newDistance, v))
        return d, prev

    def findShortestPath(self, s, e):
        d, path = self.dijktraPath(s)
        print(path)
        if path[e] == None:
            return("Not Reachable")
        finalPath = []
        i = e
        while path[i] != None:
            finalPath.append(path[i])
            i = path[i]

        return (finalPath[::-1] + [e])


g = Graph()
g.addEdge(0, 1, 3)
g.addEdge(0, 2, 6)
g.addEdge(1, 0, 3)
g.addEdge(1, 2, 2)
g.addEdge(1, 3, 1)
g.addEdge(2, 1, 6)
g.addEdge(2, 1, 2)
g.addEdge(2, 3, 1)
g.addEdge(2, 4, 4)

g.addEdge(2, 5, 2)
g.addEdge(3, 1, 1)
g.addEdge(3, 2, 1)
g.addEdge(3, 4, 2)
g.addEdge(3, 6, 4)
g.addEdge(4, 2, 4)
g.addEdge(4, 3, 2)
g.addEdge(4, 5, 2)
g.addEdge(4, 6, 1)
g.addEdge(5, 2, 2)
g.addEdge(5, 4, 2)
g.addEdge(5, 6, 1)
g.addEdge(6, 3, 4)
g.addEdge(6, 4, 1)
g.addEdge(6, 5, 1)


print(g.dijktraWeight(0))
print(g.findShortestPath(0, 6))
