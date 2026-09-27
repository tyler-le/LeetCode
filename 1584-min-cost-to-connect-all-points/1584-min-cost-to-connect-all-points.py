class UnionFind:
    def __init__ (self, n):
        self.ranks = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        self.ranks[parent_b] = parent_a
        self.sizes[parent_a]+=self.sizes[parent_b]
        self.sizes[parent_b] = 0
    
    def find(self, x):
        if x == self.ranks[x]: return x
        self.ranks[x] = self.find(self.ranks[x])
        return self.ranks[x]

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        min_heap = []
        visited = set()
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                x_i, y_i = points[i]
                x_j, y_j = points[j]

                dist = abs(x_i - x_j) + abs(y_i - y_j)
                heappush(min_heap, (dist, i, j))

        cnt = 0
        while cnt != n-1:
            dist, u, v = heappop(min_heap)
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                cnt+=1
                res+=dist
            
        return res
