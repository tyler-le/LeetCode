class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        
        def dfs(node, visited):
            
            visited.add(node)
            for nbor in graph[node]:
                if nbor not in visited:
                    dfs(nbor, visited)

            return len(visited)
        
        
        
        n = len(bombs)
        graph = defaultdict(list)
        res = 1
        
        # turn this into a graph problem
        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                u_x, u_y, u_r = bombs[i]
                v_x, v_y, _ = bombs[j]
                
                dist = sqrt((u_x - v_x)**2 + (u_y - v_y)**2)
                
                if dist <= u_r:
                    # there is a directed edge from u->v iff the distance from u->v is less than u_radius
                    graph[i].append(j)
                    
        # calculate the number of reachable nodes starting at each node i
        for i in range(n):
            visited = set()
            res = max(res, dfs(i, visited))
        
        return res
        
        