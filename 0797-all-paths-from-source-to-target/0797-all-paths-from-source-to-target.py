class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def dfs(node, path):
            nonlocal res

            if node == n-1:
                res.append(path + [node])
                return

            path.append(node)

            for nbor in graph[node]:
                dfs(nbor, path)
            
            path.pop()
            
        
        dfs(0, [])
        return res
