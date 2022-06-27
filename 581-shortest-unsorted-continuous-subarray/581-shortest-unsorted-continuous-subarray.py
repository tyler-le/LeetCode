class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        
        while l < r:
            
            while l<r and nums[l] <= nums[l+1]:
                l+=1
            while l<r and nums[r]>=nums[r-1]:
                r-=1
                
            if not l<r:
                return 0
            
            min_subarray, max_subarray = min(nums[l:r+1]), max(nums[l:r+1])
            
            while l>0 and nums[l-1] > min_subarray:
                l-=1
            while r < len(nums)-1 and nums[r+1]<max_subarray:
                r+=1
            
            return r-l+1
        
        return 0
        