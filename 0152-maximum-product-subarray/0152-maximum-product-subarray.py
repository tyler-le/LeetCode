class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prod = 1
        maxi = -float('inf')
        for i in range(n):
            prod*=nums[i]
            maxi = max(maxi, prod)
            prod = prod if prod else 1
            
        prod = 1
        for i in range(n-1, -1, -1):
            prod*=nums[i]
            maxi = max(maxi, prod)
            prod = prod if prod else 1
            
        return maxi