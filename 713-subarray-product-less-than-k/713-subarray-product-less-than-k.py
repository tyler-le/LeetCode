class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        r,l,res,product = 0,0,0,1
        
        while r < len(nums):
            product*=nums[r]
            
            while l<r and product >= k:
                    product /= nums[l]
                    l+=1
                    
            if product < k:
                res += r-l+1
                
            r+=1
        return res
        