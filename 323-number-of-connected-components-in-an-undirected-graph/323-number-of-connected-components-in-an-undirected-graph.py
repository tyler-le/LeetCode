class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = collections.defaultdict(list)
        
        for edge in edges:
            source, dest = edge[0], edge[1]
            adjacency_list[source].append(dest)
            adjacency_list[dest].append(source)
        
        
        def dfs(node, visited):
            visited.add(node)        
            
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            
        num_connected = 0
        visited = set()
        for i in range(n):
            if i not in visited: 
                dfs(i, visited)
                num_connected += 1
                
            
        return num_connected
                
            