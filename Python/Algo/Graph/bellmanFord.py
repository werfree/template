

from collections import defaultdict, deque
import heapq


class Graph():

    def __init__(self,v):
        self.V = v

        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((w, v))

    def bellman(self, s):
        graph = self.graph
        numberofvert = self.V
        dist = [float('inf')] * numberofvert
        dist[s] = 0
        for _ in range(numberofvert-1):
            for s in graph:
                for weight,node in graph[s]:
                    if dist[s] != float("inf") and dist[s]+weight<dist[node]:
                        dist[node]=dist[s]+weight

        for s in graph:
            for weight,node in graph[s]:
                if dist[s] != float("inf") and dist[s]+weight<dist[node]:
                    return("Negative cycle present")

        return dist

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


g = Graph(5)
g.addEdge(1,3,5)
g.addEdge(3,2,7)
g.addEdge(2,4,7)
g.addEdge(4,3,-15)
g.addEdge(1,2,4)
print(g.bellman(1))
