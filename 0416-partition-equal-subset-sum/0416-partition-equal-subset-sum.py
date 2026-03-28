class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        DP
        dp[x] = "can we make sum of x?"
        return dp[target]
        """

        if sum(nums) % 2: return False

        target = int(sum(nums) / 2)
        dp = [False for _ in range(sum(nums))]
        dp[0] = True

        # fix the number 
        for num in nums:
            # can we reach x?
            # if we can make (x - num), then we can make x by adding num
            for x in range(target, num - 1, -1):
                dp[x] = dp[x] or dp[x - num]


        return dp[target]


        """
        RECURSION + MEMOIZATION
        """
        n = len(nums)
        cache = {}
        def f(index, sum1, sum2):
            if index >= n: return sum1 == sum2
            if index in cache: return cache[(index, sum1, sum2)]

            cache[(index, sum1, sum2)] = True
            num = nums[index]
            if f(index + 1, sum1 + num, sum2): return True
            if f(index + 1, sum1, sum2 + num): return True

            cache[(index, sum1, sum2)] = False
            return False

        return f(0, 0, 0)
