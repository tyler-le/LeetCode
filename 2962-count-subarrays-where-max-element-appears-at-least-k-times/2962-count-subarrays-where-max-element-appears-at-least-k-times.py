class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        res = 0
        mx = max(nums)
        cnt = defaultdict(int)
        
        for r in range(n):
            cnt[nums[r]]+=1
            
            while cnt[mx] == k:
                cnt[nums[l]]-=1
                l+=1
            
            res+=l
        
        return res