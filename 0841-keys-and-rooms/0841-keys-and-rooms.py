class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # can you visit all nodes in the dag
        
        # 0 -> [1,3]
        # 1 -> [0, 1, 3]
        # 2 -> [2]
        # 3 -> [0]
        
        visited = set()
    
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nbor in rooms[node]:
                dfs(nbor)
        
        dfs(0)
        
        return len(visited) == len(rooms)
        
        
        