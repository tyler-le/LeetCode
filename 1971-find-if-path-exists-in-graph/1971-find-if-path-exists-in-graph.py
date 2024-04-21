class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build graph
        # run dfs starting on source
        # if dest is in visited -> return True
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for nbor in graph[node]:
                dfs(nbor)
        
        graph = defaultdict(list)
        visited = set()
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        dfs(source)
        return destination in visited
            
        