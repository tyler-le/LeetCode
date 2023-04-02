class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        potions.sort()
        
        for spell in spells:
            low, high = 0, len(potions) - 1
            
            while low < high:
                mid = (high + low) // 2
                if potions[mid] * spell < success:
                    low = mid + 1
                elif potions[mid] * spell >= success:
                    high = mid
                    
            if low == len(potions) or potions[low] * spell < success: 
                ret.append(0)
            else: 
                ret.append(len(potions) - low)
            
        return ret