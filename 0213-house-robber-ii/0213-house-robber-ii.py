class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(sublist):
            n = len(sublist)
            
            dp = [float('inf') for _ in range(n)]
            dp[0], dp[1] = sublist[0], max(sublist[0], sublist[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + sublist[i])
            
            return dp[-1]
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        return max(house_robber(nums[1:]), house_robber(nums[0:-1]))