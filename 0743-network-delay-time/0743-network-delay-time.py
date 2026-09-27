class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        min_heap = [(0, k)] # (dist, node)
        graph = defaultdict(list)
        visited = set()

        for u, v, w in times:
            graph[u].append((v, w))

        while min_heap:
            popped_dist, popped_node = heappop(min_heap)
            if popped_node in visited: continue
            visited.add(popped_node)
            if len(visited) == n: 
                return popped_dist

            for nbor, weight in graph[popped_node]:
                heappush(min_heap, (popped_dist + weight, nbor))

        return -1


        