class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_deletions = 0
        res = 0
        l = 0
        
        for r in range(len(nums)):
            if not nums[r]:
                num_deletions+=1
                        
            while num_deletions > 1:
                if not nums[l]: num_deletions-=1
                l+=1
                
            res = max(res, (r - l + 1 - max(1, num_deletions)))
                
            
            
        return res