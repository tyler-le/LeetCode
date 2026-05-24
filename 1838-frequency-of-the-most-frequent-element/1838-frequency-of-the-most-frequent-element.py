class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cost = 0
        n = len(nums)
        l = 0
        res = 1
        nums.sort()

        for r in range(1, n):
            cost = cost + ((nums[r] - nums[r-1]) * (r-l))

            while cost > k:
                cost-=(nums[r] - nums[l])
                l+=1
            
            if cost <= k: 
                res = max(res, r-l+1)

        return res

