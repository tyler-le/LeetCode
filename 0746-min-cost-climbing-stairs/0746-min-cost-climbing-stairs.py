class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        dp = [math.inf for _ in range(n)]
        if n == 0: return 0
        if n == 1: return cost[0]

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return dp[-1]