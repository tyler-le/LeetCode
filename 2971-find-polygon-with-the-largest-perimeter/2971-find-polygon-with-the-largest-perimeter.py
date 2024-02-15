class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        """
        The longest side of the polygon must be smaller 
        than the sum of the lengths of its other sides.
        """
        
        n, acc, longest_side, res = len(nums), 0, 0, -1
        nums.sort()
        
        for i in range(n):
            longest_side = max(longest_side, nums[i])
            acc+=nums[i]
            
            if i >= 2 and acc - longest_side > longest_side: 
                res = acc 
        
        return res
            