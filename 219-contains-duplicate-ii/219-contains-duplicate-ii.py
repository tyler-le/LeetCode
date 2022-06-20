class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count={}
        l = 0
        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)
            
            if r-l > k:
                count[nums[l]]-=1
                l+=1
        
            if count[nums[r]] >= 2:
                return True
            
        return False
                
                
            
            
        
        