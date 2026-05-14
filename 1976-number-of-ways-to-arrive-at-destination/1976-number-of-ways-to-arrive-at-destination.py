class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # number of ways to reach node with min_path
        ways = defaultdict(int) # (node : int)

        # min_path to a node
        min_path = {} # (node : int)

        graph = defaultdict(list) # (nbor, weight)

        for u, v, w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        min_heap = [(0,0)] # (dist, node)
        min_path[0] = 0
        ways[0] = 1
        MOD = 10**9 + 7

        while min_heap:
            popped_dist, popped_node = heappop(min_heap)

            for nbor, weight in graph[popped_node]:
                # if we find a new min_dist
                if nbor not in min_path or popped_dist + weight < min_path[nbor]:
                    ways[nbor] = ways[popped_node]
                    min_path[nbor] = popped_dist + weight
                    heappush(min_heap, (popped_dist + weight, nbor))

                # else we found an equal dist
                elif popped_dist + weight == min_path[nbor]:
                    ways[nbor] = (ways[nbor] + ways[popped_node]) % MOD
                    # don't push into heap since nbor is already sitting in the heap
                    # we know it's sitting in the heap because this is the second+ time we've seen this dist
                    # if we pushed it in again, we would be overcounting paths for nbor's children
        
        return ways[n-1] % MOD


