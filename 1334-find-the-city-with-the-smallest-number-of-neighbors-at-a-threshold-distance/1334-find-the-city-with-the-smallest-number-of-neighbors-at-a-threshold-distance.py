class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # for each node
            # run Dijkstras against all other nodes
            # don't add to queue if distance threshold is breached

        graph = defaultdict(list)
        reachable = defaultdict(set)

        def dijkstras(node):
            min_heap = [(0, node)] # (curr_dist, node)
            visited = set()

            while min_heap:
                popped_curr_dist, popped_node = heappop(min_heap) 
                visited.add(popped_node)

                for nbor_node, nbor_dist in graph[popped_node]:
                    dist = nbor_dist + popped_curr_dist
                    if dist > distanceThreshold: continue
                    if nbor_node in visited: continue

                    heappush(min_heap, (dist, nbor_node))
                    reachable[node].add(nbor_node)


        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        for i in range(n):
            dijkstras(i)
        
        min_cities, res = math.inf, None

        for node in range(n):
            if len(reachable[node]) <= min_cities:
                res = node
                min_cities = len(reachable[node])
        
        return res
        