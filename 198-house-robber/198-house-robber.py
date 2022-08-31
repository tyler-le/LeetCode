class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        one_house_down, two_houses_down = 0, 0
        
        for curr_house in nums:
            temp = one_house_down
            
            # calculate new previous house for next iteration
            one_house_down = max(two_houses_down + curr_house, one_house_down)
            
            # set new two_houses_down for next iteration
            two_houses_down = temp
            
        return one_house_down