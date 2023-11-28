class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        
        acc = 1
        for i in range(n):
            acc*=nums[i]
            prefix[i] = acc
            
        acc = 1
        for i in range(n-1, -1, -1):
            acc*=nums[i]
            suffix[i] = acc
            
        for i in range(n):
            if i == 0: res[i] = suffix[i+1]
            elif i == n-1: res[i] = prefix[i-1]
            else: res[i] = prefix[i-1] * suffix[i+1]
        
        return res
            
        