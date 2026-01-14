class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        goal = n - 1

        # iterate from right to left
        # 'goal' starts at last position
        # 'i' starts at second-to-last position
        # we will move 'goal' to the left as much as possible 
        # as long as 'i' can jump to it
        for i in range(n-2, -1, -1):


            # if position 'i' can jump to goal (or even past it)
            # then set the goal to 'i'
            # since it is the left most reachable position from the end
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0