class Solution:
    def numTrees(self, n: int) -> int:
        

        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for num_nodes in range(2, n+1):
            for root in range(1, num_nodes + 1):
                left = root - 1
                right = num_nodes - root

                dp[num_nodes] += dp[left] * dp[right] 
        
        return dp[-1]
                