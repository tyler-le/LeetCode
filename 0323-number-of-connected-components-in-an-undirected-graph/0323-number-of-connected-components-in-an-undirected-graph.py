class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node):
            if node in visited: return
            
            visited.add(node)
            
            for nbor in graph[node]:
                dfs(nbor)
        
        res = 0
        graph = defaultdict(list)
        visited = set()
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i)
            
        return res
        