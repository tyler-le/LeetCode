class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        curr_prod = 1

        for num in nums:
            curr_prod*=num
            res = max(res, curr_prod)
            if not curr_prod: curr_prod = 1
        
        curr_prod = 1
        for num in nums[::-1]:
            curr_prod*=num
            res = max(res, curr_prod)
            if not curr_prod: curr_prod = 1
        
        return res
