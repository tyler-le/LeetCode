class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        memo = [-1 for _ in range (n)]
        memo[0], memo[1] = 1, 2
        
        for i in range(2, n):       
                memo[i] = memo[i-1] + memo[i-2]
                
        return memo[-1]
    
        