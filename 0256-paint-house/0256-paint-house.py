class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        dp[i][j] = min cost to paint house i 
        with prev house being color j
        """
        n, m = len(costs), len(costs[0])

        dp = [[math.inf for _ in range(m)] for _ in range(n)]

        for j in range(len(costs[0])):
            dp[0][j] = costs[0][j]
        

        for i in range(1, n):
            
            for j in range(m):

                subproblem = math.inf
                for k in range(3):
                    if k != j: subproblem = min(subproblem, dp[i-1][k])
                total = costs[i][j] + subproblem
                dp[i][j] = min(dp[i][j], total)

        
        return min(dp[n-1])
        
        """
        RECURSIVE + MEMO
        f(index, prev_color) = min cost to paint house 'index' 
        with prev house being color 'prev_color'
        """
        n = len(costs)
        @cache
        def f(index, prev_color):
            if index == n: return 0
            res = math.inf

            for i in range(len(costs[index])):
                if i == prev_color: continue
                subproblem = f(index + 1, i)
                total = costs[index][i] + subproblem
                res = min(res, total)
            
            return res
        
        return f(0, None)