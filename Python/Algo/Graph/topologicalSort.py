from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        print("******BFS*****")
        visited = set()
        queue = deque()
        visited.add(s)
        queue.append(s)

        while queue:
            s = queue.popleft()
            print(s, end=' ')
            for i in self.graph[s]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        print()

    def dfs(self, s):

        print("******DFS*****")
        visited = set()

        def dfs_helper(s):
            visited.add(s)
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    return dfs_helper(i)

        dfs_helper(s)
        print()

    def topologicalSort(self):

        print("******Topological Sort******")

        visited = set()
        stack = []

        def topologicalSortHelper(s):

            visited.add(s)
            for i in self.graph[s]:
                if i not in visited:
                    topologicalSortHelper(i)
            stack.append(s)

        for i in self.graph.keys():
            if i not in visited:
                topologicalSortHelper(i)

        while stack:

            print(stack.pop(), end=" ")


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.bfs(5)
g.dfs(5)
g.topologicalSort()
