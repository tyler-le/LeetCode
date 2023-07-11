class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # create adjacency list
        graph = collections.defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        visited = set()
        res = 0
        
        def dfs(vertex):
            if vertex in visited or vertex not in graph:
                return
            visited.add(vertex)
            for nbor in graph[vertex]:
                dfs(nbor)
        
        for v in range(n):
            if v not in visited and v in graph:
                dfs(v)
                res+=1
        
        return res + (n - len(visited))
            
            