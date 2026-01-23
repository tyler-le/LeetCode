class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        if len(nums) == 1: return True
        if not nums[0]: return False
        

        for i in range(n-2, -1, -1):
            # check if we can reach the goal
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0