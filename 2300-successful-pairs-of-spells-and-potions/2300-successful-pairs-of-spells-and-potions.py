class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        potions.sort()
        p = len(potions)
        
        for spell in spells:
            low, high = 0, p - 1
            
            while low <= high:
                mid = (high + low) // 2
                if potions[mid] * spell < success:
                    low = mid + 1
                elif potions[mid] * spell >= success:
                    high = mid - 1
                    
            
            ret.append(p - low)
            
        return ret