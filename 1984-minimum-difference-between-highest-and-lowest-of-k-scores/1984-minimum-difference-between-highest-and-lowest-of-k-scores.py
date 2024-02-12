class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sort and sliding window of length k
        
        nums.sort()
        l = 0
        n = len(nums)
        res = float("inf")
        
        for r in range(n):
            if r-l+1 < k: continue
            else:
                res = min(res, nums[r] - nums[l])
                l+=1
        return res
        
