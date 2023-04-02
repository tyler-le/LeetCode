class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        out = []
        potions.sort()
        p = len(potions)
        
        for spell in spells:
            low, high = 0, p
            
            while low < high:
                mid = (high + low) // 2
                if potions[mid] * spell < success:
                    low = mid + 1
                elif potions[mid] * spell >= success:
                    high = mid
                    
            
            out.append(p - low)
            
        return out