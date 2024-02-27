class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        prefix = []
        postfix = [1 for _ in range(len(nums))]
        n = len(nums)
        res = []
        
        acc = 1
        for num in nums:
            acc*=num
            prefix.append(acc)
            
        acc = 1
        for i in range(n-1, -1, -1):
            acc*=nums[i]
            postfix[i] = acc
        
        for i in range(n):
            pre = prefix[i-1] if i-1 >=0 else 1
            post = postfix[i+1] if i+1 < n else 1
            res.append(pre*post)
        
        return res
        