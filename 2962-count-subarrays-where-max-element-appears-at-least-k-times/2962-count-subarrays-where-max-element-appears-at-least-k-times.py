class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mx_freq = 0
        l = 0
        n = len(nums)
        res = 0

        for r in range(n):
            if nums[r] == mx: mx_freq+=1

            while mx_freq == k:
                if nums[l] == mx:
                    mx_freq-=1
                l+=1
            
            res+=l
        
        return res