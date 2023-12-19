class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        
        for n in nums:
            if n < first:
                first = n
            elif n > first and n < second:
                second = n
            elif n > first and n > second:
                return True
            
        return False
        
        