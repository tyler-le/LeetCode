class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [0 for _ in range(n)]
        postfix = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        
        prefix[0], postfix[-1] = nums[0], nums[-1]
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
            
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
            
        for i in range(n):
            if i == 0:
                res[i] = postfix[i+1]
            elif i == n-1:
                res[i] = prefix[-2]
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        
        return res
        
        
            
        
        
            
        
            