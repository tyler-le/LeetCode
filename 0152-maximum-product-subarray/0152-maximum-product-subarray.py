class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod1, prod2 = 1, 1
        max1, max2 = -math.inf, -math.inf

        for num in nums:
            prod1*=num
            max1 = max(max1, prod1)
            if not prod1: prod1 = 1
        
        for num in nums[::-1]:
            prod2*=num
            max2 = max(max2, prod2)
            if not prod2: prod2 = 1

        return max(max1, max2)
        

