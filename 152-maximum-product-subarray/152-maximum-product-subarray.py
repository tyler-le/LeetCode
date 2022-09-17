class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_product, post_product, max_product = [], [], nums[0]
        
        # calculate prefix products
        curr_prod = 1
        for num in nums:
            # extend the window
            curr_prod*=num 
            
            # record the current product of the window
            pre_product.append(curr_prod)
            max_product = max(max_product, curr_prod)
            
            # reset the window if product evals to 0 for further calculations
            if curr_prod == 0: curr_prod = 1 
            
        
        
        # calculate postfix products
        curr_prod = 1
        for num in nums[::-1]:
            # extend the window
            curr_prod*=num
            
            # record the current product of the window
            post_product.append(curr_prod)
            max_product = max(max_product, curr_prod)
            
            # reset the window if product evals to 0 for further calculations
            if curr_prod == 0: curr_prod = 1
                    
        return max(pre_product + post_product)