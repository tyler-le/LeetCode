class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_flips = 0
        l = 0
        n = len(nums)
        res = 0
        
        for r in range(n):
            if not nums[r]:
                num_flips+=1
            
            while num_flips > k:
                if not nums[l]: num_flips-=1
                l+=1
            
            res = max(res, r-l+1)
        
        return res