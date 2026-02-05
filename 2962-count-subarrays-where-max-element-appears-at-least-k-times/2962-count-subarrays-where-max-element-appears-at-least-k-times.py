class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # count total subarrays n(n+1) // 2
        # count the number of subarrays where max element appears less than k times

        mx, mx_freq = max(nums), 0
        l, n = 0, len(nums)
        res = 0

        for r in range(n):
            if nums[r] == mx:
                mx_freq+=1
            
            while mx_freq == k:
                if nums[l] == mx:
                    mx_freq-=1
                l+=1

            res+=l
        
        return res