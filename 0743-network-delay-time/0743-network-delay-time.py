class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # BFS (time, node) pairs
            
        visited = {}
        
        # build adjacency matrix node : [(nbor, weight)]
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        q = deque([(k, 0)])
        
        
        while q:
            node, time = q.popleft()
            if node not in visited or time < visited[node]:
                visited[node] = time

                for nbor, weight in graph[node]:
                    q.append((nbor, time + weight))
        
        return -1 if len(visited) < n else max(visited.values())
            
        