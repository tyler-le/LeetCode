class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        res = float("inf")
        acc = 0
        
        for r in range(n):
            acc+=nums[r]
            
            while l < n and acc >= target:
                res = min(res, r-l+1)
                acc-=nums[l]
                l+=1
            
        return res if res != float("inf") else 0