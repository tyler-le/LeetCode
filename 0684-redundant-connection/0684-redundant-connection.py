class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.parents[0] = -1
        self.sizes = [1 for _ in range(n+1)]

    def find(self, x):
        if self.parents[x] == x: 
            return x
        else: 
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    # union by size 
    # if sizes[x] >= sizes[y] -> x wins
    # else sizes[x] < sizes[y] -> y wins
    def union(self, x,y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y: return
        size_x, size_y = self.sizes[par_x], self.sizes[par_y]
        if size_x >= size_y:
            self.parents[par_y] = par_x
            self.sizes[par_x]+=self.sizes[par_y]
        else:
            self.parents[par_x] = par_y
            self.sizes[par_y]+=self.sizes[par_x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for x, y in edges:
            par_x, par_y = uf.find(x), uf.find(y)
            if par_x == par_y: return [x,y]
            else: uf.union(x,y)
        
        