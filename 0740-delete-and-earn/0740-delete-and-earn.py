class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
     
        # dp[i] be the max you can earn at some value i
        
        freq = Counter(nums)
        dp = [0 for _ in range(max(nums)+1)]
        
        for num, f in freq.items():
            dp[num] = num*f
        
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        
        return dp[-1]
        