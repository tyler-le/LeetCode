class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binary search on the eating speed k
        
        low, high = 1, max(piles)
        
        while low < high: 
            
            mid = low + ((high - low) // 2)
            cnt = 0
            
            # can we eat all piles in 'h' hours with eating speed 'k' ?
            for pile in piles:
                cnt+=ceil(pile / mid)
            
            
            # decrease the eating speed
            if cnt <= h: high = mid 
                
            # increase the eating speed
            else: low = mid + 1
                
        return low
        
 