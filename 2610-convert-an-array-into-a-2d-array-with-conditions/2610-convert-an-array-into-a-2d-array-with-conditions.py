class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        hmap = Counter(nums)
        num_sets = max(hmap.values())
        sets = [set() for _ in range(num_sets)]
        
        for num in nums:
            
            for s in sets:
                
                if num not in s:
                    s.add(num)
                    break
                    
        return [list(s) for s in sets]
        
        
        
        
        