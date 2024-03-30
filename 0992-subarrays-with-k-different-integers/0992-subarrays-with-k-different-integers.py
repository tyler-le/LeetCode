class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # number of subarrays where the number of different integers is AT MOST x
        def at_most(x):
            cnt = defaultdict(int)
            n = len(nums)
            l = 0
            ans = 0
            
            for r in range(n):
                cnt[nums[r]]+=1
                
                while len(cnt) > x:
                    cnt[nums[l]]-=1
                    if not cnt[nums[l]]: del cnt[nums[l]]
                    l+=1
                
                ans+=(r-l+1)
            
            return ans
        
        return at_most(k) - at_most(k-1)