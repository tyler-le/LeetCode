class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # dijkstras (out-of-the-box) doesn't work here because of its greediness.
        # it only takes the path to a node with the cheapest price
        # but sometimes, we might want to choose a path with a larger price and fewer stops

        # hence we need to modify djikstras to add to the heap when:
            # 1. Found path w/ shorter distance (normal)
            # 2. Found path w/ less stops

        # (price, node, num_stops)
        min_heap = [(0, src, 0)]
        
        # create graph
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        prices, stops = {}, {}
        for node in range(n): 
            prices[node] = math.inf
            stops[node] = math.inf

        prices[src], stops[src] = 0, 0

        while min_heap:

            # this stop is valid, so record the min price
            popped_price, popped_node, popped_stops = heappop(min_heap)
            if popped_node == dst: return popped_price
            if popped_stops > k: continue
            
            for nbor, weight in graph[popped_node]:

                new_price = popped_price + weight
                new_stops = popped_stops + 1

                # We explore a new state IFF it improves EITHER:
                #  - we find a cheaper price, OR
                #  - fewer stops (regardless of price)

                # Inversely, we will NOT explore a path if it is 
                # - more expensive, AND 
                # - has more stops 
                # than what we've currently seen
                
                if new_price < prices[nbor] or new_stops < stops[nbor]:

                    # Update pruning thresholds.
                    # These do NOT represent the final answer.
                    # They simply mark whether future states are worth exploring (see above).
                    prices[nbor], stops[nbor] = new_price, new_stops
                    heappush(min_heap, (popped_price + weight, nbor, popped_stops + 1))
            
        return -1
            