class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        if len(nums) < 3:
            return res
        
        nums.sort()

        for index in range (0, len(nums) - 1):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            l = index + 1
            r = len(nums) - 1
            curr_sum = -nums[index]
            
            while l < r:
                if nums[l] + nums[r] == -nums[index]:
                    res.append([nums[l], nums[r], nums[index]])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                        
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                        
                
                    l+=1
                    r-=1
                
                elif nums[l] + nums[r] < -nums[index]:
                    l+=1
                    
                else:
                    r-=1
                    
        return res
        