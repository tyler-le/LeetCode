class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        # if 'i' people meet on the same node, 
        # the number of cars needed is ceil (i / seats)
        
        # for each nbor of the capital, add the result of ceil(size / seats)
        
        def dfs(curr):
            nonlocal res
            if curr in visited: return 0
            
            people = 1
            visited.add(curr)
            
            for nbor in adjacency[curr]:
                people+=dfs(nbor)
            
            if curr != capital:
                res += ceil(people / seats)
                
            return people
        
        adjacency = collections.defaultdict(list)
        visited = set()
        res = 0
        capital = 0
        
        # create adjacency matrix
        for u, v in roads:
            adjacency[u].append(v)
            adjacency[v].append(u)
        
        dfs(capital)
        return res