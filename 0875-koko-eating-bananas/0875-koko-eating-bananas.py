class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we want to optimize k (some number such that we can eat all the bananas within h hours)
        
        def solve(rate):
            hours = 0
            for pile in piles:
                if pile < rate: hours+=1
                else: hours += math.ceil(pile / rate)
            return hours <= h
        
        low, high = 1, max(piles)

        while low < high:
            mid = low + ((high - low) // 2)
            if solve(mid): high = mid
            else: low = mid + 1
        
        return high