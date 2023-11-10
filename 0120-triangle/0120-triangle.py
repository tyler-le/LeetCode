class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp, n = [], len(triangle)
        
        # initialize dp
        for i in range(1, n+1):
            dp.append([0 for _ in range(i)])
            
        # initialize dp[0][0]
        dp[0][0] = triangle[0][0]
        
        for r in range(1, n):
            m = len(triangle[r])
            
            for c in range(m):
                if c == 0:
                    dp[r][c] = triangle[r][c] + dp[r-1][0]
                elif c == (m - 1):
                    dp[r][c] = triangle[r][c] + dp[r-1][-1]
                else:
                    left, right = dp[r-1][c-1], dp[r-1][c]
                    dp[r][c] = triangle[r][c] + min(left, right)
            
        return min(dp[-1])