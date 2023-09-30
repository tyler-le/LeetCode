class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        res = 0
        left, right = 0, len(nums)-1
        
        while left < right:
            res = max(res, nums[left] + nums[right])
            left+=1
            right-=1
            
        return res