class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        n = len(graph) - 1
        
        def dfs(node, path):
            nonlocal res
            nonlocal n
            
            if node == n:
                res.append(path)
                return
            
            for nbor in graph[node]:
                path.append(nbor)
                dfs(nbor, path.copy())
                path.pop()
                
        dfs(0, [0])
        return res