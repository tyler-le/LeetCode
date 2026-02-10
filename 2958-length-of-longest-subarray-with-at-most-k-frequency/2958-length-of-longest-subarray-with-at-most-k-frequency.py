class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        n = len(nums)
        res = 0

        for r in range(n):
            cnt[nums[r]]+=1

            while cnt[nums[r]] > k:
                cnt[nums[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        
        return res