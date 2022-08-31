class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1 for _ in range(len(nums)+1)]
        memo[0], memo[1] = 0, nums[0]
        
        for i in range(1, len(nums)):
            current_house = nums[i]
            memo[i+1] = max(memo[i], memo[i-1] + current_house);

        return memo[-1]
            
