class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp[i] = min cost to get to stair i
        
        n = len(cost)
        
        dp = [float("inf") for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
            
