class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index in range (0, len(nums) - 1):
            
            # avoid duplicates
            if index > 0 and nums[index] == nums[index-1]:
                continue
                
            # two-pointer approach    
            l = index + 1
            r = len(nums) - 1
            
            # this part is 2Sum / 2Sum II. we leverage the sorted array 
            while l < r:
                target_sum = nums[l] + nums[r] + nums[index]
                
                if target_sum > 0:
                    r-=1
                    
                elif target_sum < 0:
                    l+=1
                    
                else:
                    res.append([nums[l], nums[r], nums[index]])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                        
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                        
                    l+=1
                    r-=1
                    
        return res
        