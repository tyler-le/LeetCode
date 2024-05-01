class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        # largest window that equals (sumi - x)
        sumi = sum(nums)
        l = 0
        res = -1
        n = len(nums)
        window_sum = 0
        
        for r in range(n):
            window_sum+=nums[r]
            
            while l < n and window_sum > sumi - x:
                window_sum-=nums[l]
                l+=1
            
            if window_sum == sumi - x:
                res = max(res, r-l+1)
        
        return n - res if res != -1 else res
            