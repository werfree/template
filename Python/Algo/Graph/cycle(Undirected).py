from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

        self.grapDict = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicHelper(self, s, parent, visited):
        visited.add(s)

        for i in self.graph[s]:
            if i not in visited:
                if self.isCyclicHelper(i, s, visited):
                    return True

            elif i != parent:
                return True

        return False

    def isCyclic(self):
        visited = set()

        for i in self.graph.copy():
            if i not in visited:
                if self.isCyclicHelper(i, -1, visited):
                    return True

        return False


g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(3, 4)


print(g.isCyclic())
