class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_product, post_product, max_product = [], [], nums[0]
        
        curr_prod = 1
        # calculate prefix products
        for num in nums:
            curr_prod*=num
            pre_product.append(curr_prod)
            max_product = max(max_product, curr_prod)
            
            # if the product happens to be zero, reset it to 1 so that the remaining products aren't affected
            if curr_prod == 0: curr_prod = 1
            
        
        curr_prod = 1  
        # calculate postfix products
        for num in nums[::-1]:
            curr_prod*=num
            post_product.append(curr_prod)
            max_product = max(max_product, curr_prod)
            
            # if the product happens to be zero, reset it to 1 so that the remaining products aren't affected
            if curr_prod == 0: curr_prod = 1
                    
        return max(pre_product + post_product)