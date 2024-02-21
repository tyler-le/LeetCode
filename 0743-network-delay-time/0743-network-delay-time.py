class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        hmap = defaultdict(lambda : math.inf)
        visited = set()
        q = deque([(k, 0)]) # (node : time)
        
        # create adjacency list
        for u, v, w in times:
            graph[u].append((v, w))
            
        while q:
            popped_node, popped_time = q.popleft()
            if popped_node not in visited or popped_time < hmap[popped_node]:
                hmap[popped_node] = min(popped_time, hmap[popped_node])
                visited.add(popped_node)
            
                for nbor, t in graph[popped_node]:
                    q.append((nbor, popped_time + t))
                
        return max(hmap.values()) if len(visited) == n else -1