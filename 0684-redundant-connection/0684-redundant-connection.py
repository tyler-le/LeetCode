class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        def find(node):
            while roots[node] != node:
                roots[node] = roots[roots[node]]
                node = roots[node]
            return node
        
        def union(x,y):
            p1, p2 = find(x), find(y)
            if p1 == p2: 
                return
            elif rank[p1] > rank[p2]:
                roots[p2] = roots[p1]
                rank[p1]+=rank[p2]
            else:
                roots[p1] = roots[p2]
                rank[p2]+=rank[p1]
                
        roots = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]
        
        for u, v in edges:
            if find(u) == find(v): return [u,v]
            union(u,v)
        
        # return res[-1]
            
                
                