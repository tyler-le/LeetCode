class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[1 for j in range(n)]for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i][j-1] + memo[i-1][j]
        
        return memo[m-1][n-1]