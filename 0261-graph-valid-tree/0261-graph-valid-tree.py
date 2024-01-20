class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        
        def dfs(curr, prev):
            if curr in visited: return False
            visited.add(curr)
            for nbor in graph[curr]:
                if nbor == prev: continue
                if not dfs(nbor, curr): return False
                
            return True
        
        # create adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        return dfs(0, 0) and n == len(visited)