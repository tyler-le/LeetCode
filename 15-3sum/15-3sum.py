class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index in range(len(nums) - 1):
            
            if index > 0 and nums[index]==nums[index-1]:
                continue
                
            l,r = index+1, len(nums)-1
                
            while l < r:
                target_sum = nums[index] + nums[l] + nums[r]
                
                if target_sum < 0:
                    l+=1
                    
                elif target_sum > 0:
                    r-=1
                    
                else:
                    res.append([nums[index], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                        
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                        
                    l+=1
                    r-=1
                    
        return res
        