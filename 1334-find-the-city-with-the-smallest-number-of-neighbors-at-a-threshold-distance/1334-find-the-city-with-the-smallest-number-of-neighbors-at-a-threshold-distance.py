class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        minimum_neighbors = math.inf
        res = -1

        def dijkstras(root):
            visited = set()
            min_heap = [(0, root)] # (dist, node)

            while min_heap:
                popped_dist, popped_node = heappop(min_heap)
                if popped_node in visited: continue
                if popped_dist > distanceThreshold: continue
                visited.add(popped_node)

                for nbor, edge_weight in graph[popped_node]:
                    heappush(min_heap, (popped_dist + edge_weight, nbor))

            return len(visited)

        
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        for i in range(n):
            num_neighbors = dijkstras(i)
            if num_neighbors <= minimum_neighbors:
                minimum_neighbors = num_neighbors
                res = i

        return res

        