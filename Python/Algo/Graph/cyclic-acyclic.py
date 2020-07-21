from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.whiteSet = set()
        self.blackSet = set()
        self.graySet = set()
        self.grapDict = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def hasCycle(self):
        self.whiteSet = {i for i in self.graph}
        print(self.whiteSet)


g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 4)
g.addEdge(4, 1)
g.addEdge(5, 1)

g.hasCycle()
