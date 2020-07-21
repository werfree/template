class Solution:
    def floyd(self, n, edges):

        MAX = float('inf')
        a = a = [[MAX] * n for i in range(n)]

        for u, v, w in edges:
            a[u][v] = w
            a[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # We will not check for the middle edge
                    if i == k:
                        break
                    # No self loop
                    if i == j:
                        a[i][j] = 0
                        continue
                    # dist btw u,v = min( (u,v) , [(u,k)+(k,v)] )
                    a[i][j] = min(a[i][j], a[i][k] + a[k][j])

        for i in range(n):
            print(a[i])


s = Solution()
s.floyd(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]])
