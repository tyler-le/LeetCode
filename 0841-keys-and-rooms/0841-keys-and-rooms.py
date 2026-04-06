class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        n = len(rooms)

        for src in range(n):
            for dst in rooms[src]:
                if src == dst: continue
                graph[src].append(dst)
        

        def dfs(node):
            if len(visited) == n-1: return True

            visited.add(node)

            for nbor in graph[node]:
                if nbor in visited: continue
                if dfs(nbor): return True
            
            return False

        visited = set()
        return dfs(0)