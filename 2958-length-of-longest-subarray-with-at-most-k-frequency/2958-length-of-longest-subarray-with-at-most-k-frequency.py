class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        n = len(nums)
        cnt = defaultdict(int)
        
        for r in range(n):
            cnt[nums[r]]+=1
            
            while cnt[nums[r]] > k:
                cnt[nums[l]]-=1
                if not cnt[nums[l]]: del cnt[nums[l]]
                l+=1
            
            res = max(res, r-l+1)
        
        return res
            