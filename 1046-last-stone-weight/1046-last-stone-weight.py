from heapq import heappop_max, heappush_max, heapify_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapify_max(stones)

        while len(stones) > 1:
            first, second = heappop_max(stones), heappop_max(stones)

            if first == second: continue
            else: heappush_max(stones, first - second)
        
        return stones[0] if len(stones) else 0
