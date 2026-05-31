class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        min_heap = [(0, k)]
        visited = set()
        res = 0

        for u, v, w in times:
            graph[u].append((v,w))

        while min_heap:
            popped_time, popped_node = heappop(min_heap)
            if popped_node in visited: continue
            visited.add(popped_node)
            res = popped_time

            for nbor, edge_weight in graph[popped_node]:
                heappush(min_heap, (popped_time + edge_weight, nbor))
        
        return res if len(visited) == n else -1

