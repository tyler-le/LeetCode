class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber_original(nums):
            n = len(nums)
            if n == 1: return nums[0]
            if n == 2: max(nums[0], nums[1])
                
            dp = [-1] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            
            for i in range(2,n):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
                
            return dp[-1]
        
        if len(nums) == 1: return nums[0]
        without_first = house_robber_original(nums[1:])
        without_last = house_robber_original(nums[0:-1])
        
        return max(without_first, without_last)
        