class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        
        # keep a monotonically increasing stack
        # but in the stack, we will store the index
        # but the stack will be monotonically increasing by nums[index]


        """
        For every element, 
        how far to the right can it extend 
        while remaining the minimum in that subarray?

        Use a monotonically increasing stack.
        """
        n = len(nums)
        res = 0

        # stores (index) but is increasing by nums[index]
        stack = []

        for i in range(n):
            # keep popping from stack and add to res
            while stack and nums[stack[-1]] > nums[i]:
                res+=(i - stack[-1])
                stack.pop()

            # push to stack
            stack.append(i)

        # if there are elements still in the stack,
        # this means it extends all the way to the end

        for i in stack:
            res+=(n - i)


        return res