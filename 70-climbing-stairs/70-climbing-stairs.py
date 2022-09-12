class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases start at n = 1, 2
        
        if n <= 2: return n
        
        memo = [-1 for _ in range (n+1)]
        memo[1], memo[2] = 1, 2
        
        for i in range(3, n+1):       
                memo[i] = memo[i-1] + memo[i-2]
                
        return memo[-1]