class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        res = 0
        mx = max(nums)
        freq_max = 0
        
        for r in range(n):
            if nums[r] == mx: freq_max+=1
            
            while freq_max == k:
                if nums[l] == mx: freq_max-=1
                l+=1
            
            res+=l
        
        return res