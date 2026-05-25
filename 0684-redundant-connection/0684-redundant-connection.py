class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        # self.sizes = [1 for i in range(n+1)]


    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        self.parents[y_par] = x_par
    
    def find(self, x):
        if self.parents[x] == x: 
            return x
        else: 
            root = self.find(self.parents[x])
            self.parents[x] = root
            return root


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            if uf.find(u) == uf.find(v): return [u,v]
            uf.union(u,v)
        