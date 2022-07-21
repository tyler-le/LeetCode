class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjacency_list = collections.defaultdict(list)
        
        for edge in edges:
            source, dest = edge[0], edge[1]
            adjacency_list[source].append(dest)
            adjacency_list[dest].append(source)
            
        def backtrack(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                if not backtrack(neighbor, node): return False
                
            return True
        
        return backtrack(0, -1) and len(visited) == n