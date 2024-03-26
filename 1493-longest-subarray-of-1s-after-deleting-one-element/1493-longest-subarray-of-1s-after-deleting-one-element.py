class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_mistakes = 0
        res = 0
        l = 0
        n = len(nums)
        
        for r in range(n):
            if not nums[r]: num_mistakes+=1
            
            while num_mistakes > 1:
                if not nums[l]: num_mistakes-=1
                l+=1
            
            res = max(res, r-l)
        
        return res