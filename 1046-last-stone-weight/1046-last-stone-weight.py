class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapify(stones)
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            
            if x == y: continue
            if x != y:
                y -= x
                heappush(stones, -y)
                
        return -stones[0] if stones else 0