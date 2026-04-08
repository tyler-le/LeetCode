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
        return self.find(self.ranks[x])


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # return earliest time when each node has n-1 connections

        # sort by time

        # keep adding edges into the graph

        # return when all nodes have n-1 connections (using a hashmap to track node : num edges)

        logs.sort(key = lambda x : x[0])

        # keep adding edges until all nodes are in the same component
        uf = UnionFind(n)

        for time, u, v in logs:
            parent_u, parent_v = uf.find(u), uf.find(v)
            if parent_u != parent_v: 
                uf.union(u, v)
            
            if uf.sizes[uf.find(u)] == n:
                return time
        
        return -1


