class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        l = 0
        n = len(nums)
        res = math.inf

        for r in range(n):
            curr_sum+=nums[r]
            while curr_sum >= target:
                res = min(res, r-l+1)
                curr_sum-=nums[l]
                l+=1
        
        return res if res != math.inf else 0