class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, n = 0, len(nums)
        mx, mx_freq = max(nums), 0
        res = 0

        for r in range(n):
            num = nums[r]
            if num == mx:
                mx_freq+=1
            
            while mx_freq >= k:
                if nums[l] == mx:
                    mx_freq-=1
                l+=1
            
            if mx_freq == k-1:
                res+=l
        
        return res
            
