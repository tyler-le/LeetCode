class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        n = len(nums)
        res = 0
        mx = max(nums)
        
        for r in range(n):
            cnt[nums[r]]+=1

            while cnt[mx] == k:
                cnt[nums[l]]-=1
                if not cnt[nums[l]]: del cnt[nums[l]]
                l+=1
                res+=n-r
            
            # # res+=l is counting the number of subarrays that END AT index r
            # res+=l
                
                
        return res
            
        
        