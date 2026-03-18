class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        res = -math.inf

        for num in nums:
            if curr_sum + num < num:
                curr_sum = num
            else:
                curr_sum+=num
            
            res = max(res, curr_sum)
        
        return res