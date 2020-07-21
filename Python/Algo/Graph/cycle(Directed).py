from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

        self.grapDict = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicHelper(self, s, visited, recStack):
        visited.add(s)
        recStack.add(s)

        for i in self.graph[s]:
            if i not in visited:
                if self.isCyclicHelper(i, visited, recStack):
                    return True
            elif i in recStack:
                return True
        recStack.remove(s)
        return False

    def isCyclic(self):
        visited = set()
        recStack = set()
        for i in self.graph.copy():
            if i not in visited:
                if self.isCyclicHelper(i, visited, recStack):
                    print(recStack)
                    return True
        return False


g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 4)


print(g.isCyclic())
