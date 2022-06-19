class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        count = [0,0]
        max_len = l = 0
        
        for r in range(len(nums)):
            count[nums[r]] += 1
            if (r-l+1) - count[1] > k:
                count[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            
        return max_len
        
        