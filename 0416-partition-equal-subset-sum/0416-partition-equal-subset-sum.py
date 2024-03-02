class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sumi, n = sum(nums), len(nums)
        dp = [[False for _ in range(sumi + 1)] for _ in range(n+1)]
        n, m = len(dp), len(dp[0])
        if sumi % 2: return False
        for i in range(n):
            dp[i][0] = True
            
        for i in range(1, n):
            for j in range(1, m):
                
                # can we make sum 'j' when including i'th element
                include = False if j - nums[i-1] < 0 else dp[i-1][j - nums[i-1]]
                
                # can we make sum 'j' when excluding i'th element
                exclude = dp[i-1][j]
                
                dp[i][j] = include or exclude
        
        return dp[-1][sumi // 2]