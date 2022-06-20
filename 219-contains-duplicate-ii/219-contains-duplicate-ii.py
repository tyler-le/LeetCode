class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count={}
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                count[nums[l]]-=1
                l+=1
                
            if nums[r] in count and count[nums[r]] > 0:
                return True
            
            count[nums[r]] = 1
            
            
            
        return False
                
                
            
            
        
        