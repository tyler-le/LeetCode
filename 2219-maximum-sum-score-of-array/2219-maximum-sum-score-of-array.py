class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        res = -float("inf")
        
        for i, num in enumerate(nums):
            right_sum = S - left_sum
            left_sum+=num
            res = max(res, right_sum, left_sum)
        
        return res
            