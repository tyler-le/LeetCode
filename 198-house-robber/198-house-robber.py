class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        memo = [-1 for _ in range(len(nums))]
        memo[0], memo[1] = nums[0], max(nums[0], nums[1])
    
        for i in range(2, len(nums)):
            one_house_before = memo[i-1]
            two_houses_before = memo[i-2]
            current_house = nums[i]
            # curr house is the max(loot of prev house, loot of two houses down and rob current house )
            memo[i] = max(one_house_before, two_houses_before + current_house)
            
        return memo[-1]
            
