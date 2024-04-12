class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # return all the source nodes?
        indegrees = {}
        res = []
        
        for u, v in edges:
            if u not in indegrees: indegrees[u] = 0
            if v not in indegrees: indegrees[v] = 1
            else: indegrees[v]+=1
        
        for n, x in indegrees.items():
            if not x: res.append(n)
        
        return res