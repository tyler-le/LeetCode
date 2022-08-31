class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1 for _ in range(len(nums)+1)]
        
        def dp(i):
            if i < 0: return 0
            # check if we've found the result for this index already
            if memo[i] > 0: return memo[i] 
            memo[0] = 0
            memo[1] = nums[0]
            
            for i in range(1, len(nums)):
                current_house = nums[i]
                memo[i+1] = max(memo[i], memo[i-1] + current_house);
            
            return memo[-1]
            
        return dp(len(nums)-1)