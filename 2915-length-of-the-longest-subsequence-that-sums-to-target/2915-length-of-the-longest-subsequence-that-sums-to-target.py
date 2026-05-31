class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n, m = len(nums), target
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[n][0] = 0

        for i in range(n-1, -1, -1):
            for j in range(m, -1, -1):
                exclude = dp[i+1][j]
                include = -1
                if j - nums[i] >= 0:
                    prev = dp[i+1][j-nums[i]]
                    if prev != -1:
                        include = prev + 1
                
                dp[i][j] = max(include, exclude)

        return dp[0][m]

        
        n = len(nums)

        @cache
        def f(index, curr, path_len):
            
            if curr > target: return -1
            if curr == target: return path_len
            if index == n: return -1

            include = f(index + 1, curr + nums[index], path_len + 1)
            exclude = f(index + 1, curr, path_len)

            return max(include, exclude)

        return f(0, 0, 0)