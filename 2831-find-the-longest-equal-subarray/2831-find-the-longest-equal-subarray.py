class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        
        l = 0
        res = 0
        cnt = defaultdict(int)
        n = len(nums)
        max_freq = -math.inf
        
        for r in range(n):
            cnt[nums[r]]+=1
            max_freq = max(max_freq, cnt[nums[r]])
            
            # while max(cnt.values()) - (r-l+1) > k:
            while r-l+1 - max_freq > k:
                cnt[nums[l]]-=1
                if not cnt[nums[l]]: del cnt[nums[l]]
                l+=1
            
            res = max(res, max_freq)
        
        return res