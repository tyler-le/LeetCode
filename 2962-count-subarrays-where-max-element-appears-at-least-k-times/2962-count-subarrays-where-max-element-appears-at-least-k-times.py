class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        n = len(nums)
        mx, mx_cnt = max(nums), 0

        for r in range(n):
            # add to the window
            if nums[r] == mx: mx_cnt+=1

            # shrink the window
            while mx_cnt == k:
                if nums[l] == mx: mx_cnt-=1
                l+=1

            # record the result
            res+=l
        
        return res