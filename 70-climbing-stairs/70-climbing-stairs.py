class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Recursion w/ memoization
        memo = [-1 for _ in range(n+1)]
        
        def helper(n):
            if n == 1: return 1
            if n == 2: return 2
            
            # if we already calculated subproblem
            if memo[n] != -1: return memo[n]
            
            # else recursively calculate subproblem
            res = helper(n-1) + helper(n-2)
            memo[n] = res
            
            return memo[n]
        
        return helper(n)
        