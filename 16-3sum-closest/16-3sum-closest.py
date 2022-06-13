import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = sys.maxint
        curr_sum = 0
        nums.sort()
        
        for index in range(0, len(nums)-1):
            l = index + 1
            r = len(nums) - 1
            print(index)
            
            while l < r:
                if nums[index] + nums[l] + nums[r] == target:
                    return target
                
                elif nums[index] + nums[l] + nums[r] < target:
                    if abs(target - (nums[index] + nums[l] + nums[r])) < closest:
                        closest = abs(target - (nums[index] + nums[l] + nums[r]))
                        curr_sum = (nums[index] + nums[l] + nums[r])
                    l+=1
                    
                elif nums[index] + nums[l] + nums[r] > target:
                    if abs(target - (nums[index] + nums[l] + nums[r])) < closest:
                        closest = abs(target - (nums[index] + nums[l] + nums[r]))
                        curr_sum = (nums[index] + nums[l] + nums[r])    
                    r-=1
                    
                    
        return curr_sum