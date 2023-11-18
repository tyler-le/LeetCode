class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rows = len(nums) + 1
        cols = sum(nums) + 1
        
        if sum(nums) % 2: return False
        
        dp = [[False for _ in range(cols)] for _ in range(rows)]
                    
        for r in range(rows): dp[r][0] = True
            
        for i in range(1, rows):
            for j in range(1, cols):
                
                exclude = dp[i-1][j]
                
                if j - nums[i-1] < 0: include = False
                else: include = dp[i-1][j-nums[i-1]]
                    
                dp[i][j] = include or exclude

        return dp[-1][sum(nums) // 2]
        
        