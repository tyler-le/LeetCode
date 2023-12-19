class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] is the length of the LIS ending at index i
        # return max(dp)
        
        n = len(nums)
        dp = [0 for _ in range(n)]
       
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
        return max(dp) + 1