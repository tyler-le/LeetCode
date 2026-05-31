class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n, m = len(nums), target
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(m+1):
                num = nums[i-1]
                include = dp[i-1][j - num] if j - num >= 0 else -1
                if include != -1: include+=1
                exclude = dp[i-1][j]
                dp[i][j] = max(include, exclude)

        return dp[n][target]

        
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