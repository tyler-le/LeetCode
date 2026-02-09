class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [math.inf for _ in range(n+1)] # dp[n] is the top
        
        # dp[i] = cost to reach step i
        dp[0] = 0 # we can start here for free
        dp[1] = 0 # we can start here for free

        for i in range(2, n+1):
            one_step = dp[i-1] + cost[i-1] # how much it took to reach step i-1 and the cost to jump from i-1 to i
            two_step = dp[i-2] + cost[i-2] # how much it took to reach step i-2 and the cost to jump from i-2 to i
            dp[i] = min(two_step, one_step)

        return dp[n]