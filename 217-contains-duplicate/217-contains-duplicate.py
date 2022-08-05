class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        butts = set()
        
        for num in nums:
            if num in butts:
                return True
            else:
                butts.add(num)
            
        return False
            