class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = [0] * (n+1)
        memo[0] = memo[1] = 1
        
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[-1]
        