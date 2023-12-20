class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        adjacency = defaultdict(list)
        q = deque([0])
        res = 0
        visited = set()
        restricted = set(restricted)
        
        # build adjacency matrix
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
            
        while q:
            res+=1
            popped = q.popleft()
            visited.add(popped)
            for nbor in adjacency[popped]:
                if nbor in restricted or nbor in visited: continue
                q.append(nbor)
            
        return res
            
            
            
        
            
        
            