class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        # if 's' is a an odd number, we can't have two subsets with same total
        if s % 2 != 0: return False

        # we are trying to find a subset of given numbers that has a total sum of 's/2'.
        s = int(s / 2)

        n = len(nums)
        dp = [[False for x in range(s+1)] for y in range(n)]

        # populate the s=0 columns, as we can always for '0' sum with an empty set
        for i in range(0, n):
            dp[i][0] = True

      # with only one number, we can form a subset only when the required sum is
      # equal to its value
        for j in range(1, s+1):
            dp[0][j] = nums[0] == j

        for i in range(1, n):
          for j in range(1, s+1):        
            IN = dp[i-1][j-nums[i]] if (j-nums[i] >= 0) else False
            OUT = dp[i-1][j]
            dp[i][j] = IN or OUT

        return dp[n - 1][s]

