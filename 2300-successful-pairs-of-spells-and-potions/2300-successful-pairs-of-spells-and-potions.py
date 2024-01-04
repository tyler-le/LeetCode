class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # for each spell, binary search to find the minimum value that is successful
        res = []
        potions.sort()
        
        def binary_search(spell):
            low, high = 0, len(potions) - 1
            
            while low <= high:
                mid = low + ((high - low) // 2)
                if spell * potions[mid] >= success: high = mid - 1
                else: low = mid + 1
            
            return high
        
        
        for spell in spells:
            res.append(len(potions) - binary_search(spell) - 1)
            
        
        return res
    
    
    