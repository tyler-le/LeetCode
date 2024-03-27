class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        n = len(nums)
        acc = 1
        
        for r in range(n):
            acc*=nums[r]
            
            while l <= r and acc >= k:
                acc/=nums[l]
                l+=1
            
            if l<=r and acc < k: res+=(r-l+1)
        
        return res
            