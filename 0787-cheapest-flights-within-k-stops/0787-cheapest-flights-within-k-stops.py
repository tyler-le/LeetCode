class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        stops = [math.inf for _ in range(n)]
        prices = [math.inf for _ in range(n)]
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        min_heap = [(0, src, 0)] # price, node, num_stops)
        visited = set()

        while min_heap:
            popped_price, popped_node, popped_stops = heappop(min_heap)

            if popped_node == dst and popped_stops - 1 <= k: 
                return popped_price

            # if popped_node in visited: continue
            # visited.add(popped_node)

            for nbor, edge_weight in graph[popped_node]:
                if popped_price + edge_weight <= prices[nbor] or popped_stops + 1 <= stops[nbor]:

                    heappush(min_heap, (popped_price + edge_weight, nbor, popped_stops + 1))
                    prices[nbor] = popped_price + edge_weight
                    stops[nbor] = popped_stops + 1

        return -1

            
        