class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        acc = 0
        longest_side = 0
        res = -1
        # The longest side of the polygon must be smaller 
        # than the sum of the lengths of its other sides.

        for i in range(n):
            num = nums[i]
            longest_side = max(longest_side, num)
            acc+=num
            if i >= 2 and acc - longest_side > longest_side: 
                res = acc 
        
        return res
            