class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2: return False
        
        ROWS, COLS = len(nums), (sum(nums) // 2) + 1
        
        dp = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
        for i in range(ROWS):
            dp[i][0] = True
            
        for i in range(1, ROWS):
            for j in range(1, COLS):
                
                if nums[i] <= j: include = dp[i-1][j - nums[i]] 
                else: include = False
                
                exclude = dp[i-1][j]
        
                dp[i][j] = include or exclude
            
        return dp[-1][sum(nums) // 2]