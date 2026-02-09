class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [math.inf for _ in range(n+1)] # dp[n] is the top
        
        # dp[i] = cost to reach step i
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            one_step = dp[i-1] + cost[i-1]
            two_step = dp[i-2] + cost[i-2]
            dp[i] = min(two_step, one_step)

        return dp[n]