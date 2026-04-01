class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        n = len(graph)
        bad = set()        
        cache = {}

        def has_cycle(node) -> bool:

            if node in cache: return cache[node]

            if node in visited:
                # bad.update(visited)
                cache[node] = True
                return True
            
            if not graph[node]:
                cache[node] = False
                return False

            visited.add(node)

            for nbor in graph[node]:
                if has_cycle(nbor):
                    bad.update(visited)
                    cache[node] = True
                    return True
            
            visited.remove(node)
            cache[node] = False
            return False
            
        
        for node in range(n):
            if node in visited: continue
            has_cycle(node)
        
        return sorted(set(range(n)) - bad)



