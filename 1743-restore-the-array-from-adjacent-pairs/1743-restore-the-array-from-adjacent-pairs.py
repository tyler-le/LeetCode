class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming_edges = defaultdict(int)
        res = []
        q = deque()
        visited = set()
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
            incoming_edges[u]+=1
            incoming_edges[v]+=1
            
        for node, incoming in incoming_edges.items():
            if incoming == 1:
                q.append(node)
                break
                
        while q:
            popped_node = q.popleft()
            res.append(popped_node)
            visited.add(popped_node)
            for nbor in graph[popped_node]:
                if nbor not in visited:
                    q.append(nbor)
        
        return res