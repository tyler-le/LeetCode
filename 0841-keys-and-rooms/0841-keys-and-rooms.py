class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        
        def dfs(node):
            
            if node in visited: return
            
            visited.add(node)
            
            for room in rooms[node]:
                dfs(room)
        
        dfs(0)
        
        return len(visited) == len(rooms)