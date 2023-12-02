class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        res = -float("inf")
        
        while l < r:
            res = max(res, nums[l] + nums[r])
            l+=1
            r-=1
            
        return res