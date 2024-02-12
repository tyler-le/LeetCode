class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_biggest, second_biggest = -float("inf"), -float("inf")
        
        for num in nums:
            if num >= first_biggest: 
                second_biggest = first_biggest
                first_biggest = num
                
            if num > second_biggest and num < first_biggest:
                second_biggest = num
                
        return (first_biggest - 1) * (second_biggest - 1)