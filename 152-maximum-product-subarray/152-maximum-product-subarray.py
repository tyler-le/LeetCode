class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_prod = 1
        pre_product, post_product = [], []
        max_product = nums[0]
        
        for num in nums:
            curr_prod*=num
            pre_product.append(curr_prod)
            max_product = max(max_product, curr_prod)
            if not curr_prod: curr_prod = 1
            
        
        curr_prod = 1    
        for num in nums[::-1]:
            curr_prod*=num
            post_product.append(curr_prod)
            max_product = max(max_product, curr_prod)
            if not curr_prod: curr_prod = 1
                    
        return max(nums+pre_product+post_product)