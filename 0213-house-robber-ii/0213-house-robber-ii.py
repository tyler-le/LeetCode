class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def rob(sublist):
            # dp[i] = max(dp[i-1] , dp[i-2] + nums[i])

            dp = [0 for _ in range(len(sublist))]
            dp[0] = sublist[0]
            dp[1] = max(sublist[0], sublist[1])

            for i in range(2, len(sublist)):
                dp[i] = max(dp[i-1], dp[i-2] + sublist[i])

            return dp[-1]

        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        return max(rob(nums[:n-1]), rob(nums[1:]))