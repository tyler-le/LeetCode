class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumi = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == sumi - num - left_sum:
                return i
            left_sum+=num
        return -1
        