class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        suffix = [1 for _ in range(n)]
        res = []
        
        # prefix = [1 2 6 24]
        # suffix = [24 24 12 4]
        
        acc = 1
        for num in nums:
            acc*=num
            prefix.append(acc)
        
        acc = 1
        for i in range(n-1, -1, -1):
            acc*=nums[i]
            suffix[i] = acc
        
        for i in range(n):
            pre = prefix[i-1] if i-1 >=0 else 1
            suf = suffix[i+1] if i+1 < n else 1
            res.append(pre*suf)
        
        return res