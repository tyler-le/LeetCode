class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        curr_sum = 0
        for num in nums:
            # add to subarray or restart
            if curr_sum + num < num: 
                curr_sum = num
            else:
                curr_sum+=num
            
            res = max(res, curr_sum)
        
        return res

