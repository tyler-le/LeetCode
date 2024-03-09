class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_smallest, second_smallest = math.inf, math.inf
        
        for num in nums:
            if num <= first_smallest:
                first_smallest = num
            elif num > first_smallest and num <= second_smallest:
                second_smallest = num
            else:
                return True
        
        return False