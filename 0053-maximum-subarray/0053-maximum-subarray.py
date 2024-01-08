class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # keep adding until the subarray unless we can reset to a new element
        
        curr_sum = nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            
            if num > curr_sum + num:
                curr_sum = num
            else:
                curr_sum+=num
                
            res = max(res, curr_sum)
        
        return res
            