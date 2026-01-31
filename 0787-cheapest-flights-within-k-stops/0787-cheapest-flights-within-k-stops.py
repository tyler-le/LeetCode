class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        min_heap = [(0, 0, src)] # cost, num_stops, node
        res = math.inf
        min_costs_seen = [math.inf for _ in range(n)]
        min_stops_seen = [math.inf for _ in range(n)]
        

        for u, v, w in flights:
            graph[u].append((v, w))
        
        while min_heap:
            popped_cost, popped_stops, popped_node = heappop(min_heap)

            if popped_node == dst: 
                res = min(res, popped_cost)
                continue

            for nbor_node, nbor_cost in graph[popped_node]:
                cost = popped_cost + nbor_cost
                stops = popped_stops + 1
                
                if stops > k + 1: continue
                
                if cost < min_costs_seen[nbor_node] or stops < min_stops_seen[nbor_node]:
                    # print(f"found a more optimal path")
                    min_costs_seen[nbor_node] = cost
                    min_stops_seen[nbor_node] = stops
                    heappush(min_heap, (cost, stops, nbor_node))

        return res if res != math.inf else -1               
                