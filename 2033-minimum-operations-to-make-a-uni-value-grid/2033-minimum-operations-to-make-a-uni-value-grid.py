class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # calculate the number of operations to get all elements to the median element

        nums = []
        n, m = len(grid), len(grid[0])
        res = 0

        for i in range(n):
            for j in range(m):
                nums.append(grid[i][j])

        nums.sort()
        median = nums[len(nums) // 2]

        # check if possible
        for num in nums:

            # cannot reach median by adding or subtract x any number of times
            if ( median - num ) % x:
                return -1

        for num in nums:

            # count number of operations to go from num to median in increments of x
            res+= ( abs(median - num) // x )

        return res
