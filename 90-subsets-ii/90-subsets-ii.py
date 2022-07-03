class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        power_set = []
        power_set.append([])
        added_last_step = 0
        
        for i in range(len(nums)):
            
            current_level = []
            if i > 0 and nums[i] == nums[i-1]:
                for j in range(len(power_set) - added_last_step, len(power_set)):
                    new_subset = power_set[j] + [nums[i]]
                    current_level.append(new_subset)
                    
                    
            else:
                for subset in power_set:
                    new_subset = subset + [nums[i]]
                    current_level.append(new_subset)
                
            power_set += current_level
            added_last_step = len(current_level)
            
        return power_set
            

        
        
        