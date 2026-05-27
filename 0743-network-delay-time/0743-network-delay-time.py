class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        res = 0

        # create graph
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))

        # create heap queue
        min_heap = [(0, k)] # (distance, node)
        visited = set()


        # run dijkstras from the source
        while min_heap:
            popped_dist, popped_node = heappop(min_heap)
            if popped_node in visited: continue
            visited.add(popped_node)
            res = popped_dist
            
            for nbor, edge_weight in graph[popped_node]:
                heappush(min_heap, (popped_dist + edge_weight, nbor))

            

        # if we visited all nodes -> return res
        # else -> return -1
        return res if len(visited) == n else -1