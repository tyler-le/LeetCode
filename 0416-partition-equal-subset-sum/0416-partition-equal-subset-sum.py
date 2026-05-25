class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        m = total // 2
        n = len(nums)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]

        dp[n][m] = True


        for i in range(n-1, -1, -1):
            for j in range(m, -1, -1):
                num = nums[i]
                first_choice = dp[i+1][j+num] if i+1 <= n and j+num <= m else False
                second_choice = dp[i+1][j] if i+1 <= n else False
                dp[i][j] = first_choice or second_choice

        return dp[0][0]
        
        
        
        target = sum(nums) / 2
        if (target * 2) != sum(nums): return False
        n = len(nums)
        nums.sort(reverse=True)

        @cache
        def backtrack(index, path_sum):
            if index >= n: 
                if path_sum == target: return True
                return False
            if path_sum > target: return False

            num = nums[index]
            first_choice = backtrack(index + 1, path_sum + num)
            second_choice = backtrack(index + 1, path_sum)

            return first_choice or second_choice

        return backtrack(0, 0)

