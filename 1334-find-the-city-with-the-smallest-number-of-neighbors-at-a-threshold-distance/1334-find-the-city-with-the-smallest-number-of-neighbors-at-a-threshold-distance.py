class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        res = []
        reachable = defaultdict(set)

        def dijkstras(node):
            min_heap = [(0, node)] # (travel_cost, node)
            visited = set()

            while min_heap:
                popped_cost, popped_node = heappop(min_heap)
                visited.add(popped_node)
                
                for nbor_node, nbor_weight in graph[popped_node]:
                    new_cost = nbor_weight + popped_cost
                    if new_cost > distanceThreshold: continue
                    if nbor_node in visited: continue
                    heappush(min_heap, (new_cost, nbor_node))
                    reachable[node].add(nbor_node)
        
        # 1. build graph
        graph = defaultdict(list) # (nbor, weight)
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        # 2. run dijkstras for each node
        for i in range(n):
            dijkstras(i)

        # 3. process cities 
        mn = min(len(x) for x in reachable.values())
        for i in range(n-1, -1, -1):
            if len(reachable[i]) == mn: return i