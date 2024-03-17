class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # loop thru nums
        # if it's better to restart, then restart
        # track max each iteration
        
        acc = nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            
            if num > acc + num:
                acc = num
            else:
                acc+=num
                
            res = max(res, acc)
        
        return res
        