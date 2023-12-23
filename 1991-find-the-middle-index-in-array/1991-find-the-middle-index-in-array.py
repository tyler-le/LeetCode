class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == S - num - left_sum:
                return i
            left_sum+=num
        return -1
            