class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, postfix_prod = 1, 1
        prefix, postfix = [], []
        res, n = [1 for num in nums], len(nums)
        
        for num in nums:
            prefix_prod*=num
            prefix.append(prefix_prod)
        
        for num in nums[::-1]:
            postfix_prod*=num
            postfix.append(postfix_prod)
            
        for i in range(n):
            if i == 0: res[i] = postfix[-2]
            elif i == n - 1: res[i] = prefix[i - 1]
            else: res[i] = prefix[i-1]*postfix[n - i - 2]
            
        print(prefix, postfix)
        return res
        