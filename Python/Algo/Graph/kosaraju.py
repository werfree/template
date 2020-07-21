

from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s, visited, stack):
        visited.add(s)

        for i in self.graph[s]:
            if i not in visited:
                self.dfs(i, visited, stack)

        stack.append(s)

    def print_dfs(self, s, visited, graph, ans):
        visited.add(s)
        print(s, end=" ")
        ans[-1].append(s)

        for i in graph[s]:
            if i not in visited:
                self.print_dfs(i, visited, graph, ans)

    def transpose(self):
        transposeGraph = Graph()
        for i in self.graph:
            for j in self.graph[i]:
                transposeGraph.addEdge(j, i)

        return transposeGraph.graph

    def kosaraju(self):

        # Step 1  ---- DFS

        visited = set()
        stack = []

        for i in self.graph.copy():
            if i not in visited:
                self.dfs(i, visited, stack)

        # Step 2 ---- Transpose

        transposeGraph = self.transpose()

        # Step 3 ----- Pop Stack and DFS on It
        visited = set()
        ans = []
        while stack:
            i = stack.pop()
            if i not in visited:
                ans.append([])
                self.print_dfs(i, visited, transposeGraph, ans)
                print()

        return ans


g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 4)
g.addEdge(7, 6)
g.addEdge(7, 8)


print(g.kosaraju())

# Thanks to Divyanshu Mehta for contributing this code
