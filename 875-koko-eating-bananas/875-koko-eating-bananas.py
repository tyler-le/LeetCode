class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        
        while low < high:
            
            # check if mid is a valid eating speed
            # if it is, set high = mid - 1
            # else set low = mid + 1
            
            total_hours = 0
            eating_speed = low + ( (high - low) // 2 )
            
            for pile in piles:
                total_hours += math.ceil(pile / eating_speed)
            
            if total_hours <= h: high = eating_speed
            else: low = eating_speed + 1
                
        return high
            
            