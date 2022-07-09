class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_before, product_after, answer = [], [0] * len(nums), []
        
        curr_prod = 1
        for num in nums:
            curr_prod *= num
            product_before.append(curr_prod)
        
        curr_prod = 1
        for i in range(len(nums)-1, -1, -1):
            curr_prod *= nums[i]
            product_after[i] = curr_prod
            
        for i in range(len(nums)):
            if i == 0:
                answer.append(product_after[i+1])
            elif i == len(nums)-1:
                answer.append(product_before[i-1])
            else:
                answer.append(product_after[i+1] * product_before[i-1])
                
        return answer
            
        