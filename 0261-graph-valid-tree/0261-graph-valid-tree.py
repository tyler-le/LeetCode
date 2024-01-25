class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(prev, curr):
            res = False
            if curr in visited: return False
            visited.add(curr)
            
            for nbor in graph[curr]:
                if nbor == prev: continue
                if not dfs(curr, nbor):
                    return False
            
            return True
        
        return dfs(0, 0) and len(visited) == n
        