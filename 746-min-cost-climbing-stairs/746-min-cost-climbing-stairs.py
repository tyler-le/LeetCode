class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def min_cost(i):
            if i < 0: return 0
            if i == 0 or i == 1: return cost[i]
            if memo[i] != -1: return memo[i]
            
            res = cost[i] + min(min_cost(i-1), min_cost(i-2))
            memo[i] = res
            return res
        
        memo = [-1 for _ in range (len(cost))]
        n = len(cost)
        return min(min_cost(n-1), min_cost(n-2))
    
            