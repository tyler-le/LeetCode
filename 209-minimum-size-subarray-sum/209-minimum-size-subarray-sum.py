class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while l < len(nums) and curr_sum >= target:
                min_size = min(min_size, r-l+1)
                curr_sum -= nums[l]
                l+=1
                
        return min_size if (min_size != float('inf')) else 0