class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        nums.sort()

        for index in range (0, len(nums) - 1):
            
            # avoid duplicates
            if index > 0 and nums[index] == nums[index-1]:
                continue
                
            # two-pointer approach    
            l = index + 1
            r = len(nums) - 1
            curr_sum = -nums[index]
            
            # this part is 2Sum / 2Sum II. we leverage the sorted array 
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
        