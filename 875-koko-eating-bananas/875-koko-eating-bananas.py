class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 0, max(piles)
        
        while low < high:
            mid = low + ( (high - low) // 2 )
            
            # check if mid is a valid eating speed
            # if it is, set high = mid - 1
            # else set low = mid + 1
            
            total_hours = 0
            eating_speed = mid
            
            for pile in piles:
                if mid == 0: return 1
                total_hours += math.ceil(pile / eating_speed)
            
            if total_hours <= h:
                high = mid
                
            else:
                low = mid + 1
                
        return high
            
            