class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # alternative solution - use union find and an edge should not be part of two components
        # for each edge (u, v) in the graph, we find the parent, p, of the sets containing u and v using the find operation
        # if u and v have the same parent, there must be a cycle because u ~> p and v ~> p so there is a cycle u ~> p <~ v
        
        class UnionFind():
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return True  # Indicates a cycle
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1
                return False
        
        
        uf = UnionFind(n)
        num_components = n
        
        for u, v in edges:
            if uf.find(u) == uf.find(v): 
                return False
            else: 
                uf.union(u, v) 
                num_components-=1
             
        return num_components == 1
            
        