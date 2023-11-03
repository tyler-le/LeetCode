class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = low + (high - low) // 2
            total_hours = 0
            
            for pile in piles:
                total_hours += math.ceil(pile / mid)
                
            if total_hours <= h: high = mid
            else: low = mid + 1
                
        return low