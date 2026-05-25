class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)        
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]

        """
        corresponds to this base case in recursive sol:
            if index >= n: 
                if path_sum == target: return True
            
        """
        dp[n][target] = True

        for i in range(n-1, -1, -1):
            for path_sum in range(target, -1, -1):
                num = nums[i]
                first_choice = dp[i+1][path_sum+num] if i+1 <= n and path_sum+num <= target else False
                second_choice = dp[i+1][path_sum] if i+1 <= n else False
                dp[i][path_sum] = first_choice or second_choice

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

