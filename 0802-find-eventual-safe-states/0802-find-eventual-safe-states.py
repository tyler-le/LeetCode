class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        n = len(graph)
        bad = set()        
        cache = {}
        safe_nodes = {}

        def dfs(node) -> bool:

            if node in safe_nodes: 
                return safe_nodes[node]

            if node in visited:
                safe_nodes[node] = False
                return False

            visited.add(node)

            for nbor in graph[node]:
                if not dfs(nbor):
                    safe_nodes[node] = False
                    return False
            
            visited.remove(node)
            safe_nodes[node] = True
            return True
            
        
        for node in range(n):
            if node in visited: continue
            dfs(node)
        
        res = []

        for i in range(n):
            if safe_nodes[i]: res.append(i)

        return res