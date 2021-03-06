
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_dist = float('inf')
        curr_sum = 0
        nums.sort()
        
        for index in range(0, len(nums)-1):
            l = index + 1
            r = len(nums) - 1
            
            while l < r:
                if nums[index] + nums[l] + nums[r] == target:
                    return target
                
                elif nums[index] + nums[l] + nums[r] < target:
                    if abs(target - (nums[index] + nums[l] + nums[r])) < min_dist:
                        min_dist = abs(target - (nums[index] + nums[l] + nums[r]))
                        curr_sum = (nums[index] + nums[l] + nums[r])
                    l+=1
                    
                elif nums[index] + nums[l] + nums[r] > target:
                    if abs(target - (nums[index] + nums[l] + nums[r])) < min_dist:
                        min_dist = abs(target - (nums[index] + nums[l] + nums[r]))
                        curr_sum = (nums[index] + nums[l] + nums[r])    
                    r-=1
                    
                    
        return curr_sum