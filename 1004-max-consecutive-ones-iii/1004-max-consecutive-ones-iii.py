class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        l = 0
        n = len(nums)
        res = 0

        for r in range(n):
            # add to the window
            if nums[r] == 0: num_zeros+=1
            
            # shrink the window
            while num_zeros > k:
                if nums[l] == 0: num_zeros-=1
                l+=1
            
            # record the result
            res = max(res, r-l+1)
        
        return res
            
