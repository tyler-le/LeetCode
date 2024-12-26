class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n - 2):
            first, second, third = nums[i], nums[i+1], nums[i+2]
            res+= (first + third == second / 2)
        
        return res
        