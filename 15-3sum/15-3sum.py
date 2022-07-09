class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-1):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j, k, target = i+1, len(nums)-1, -nums[i]
                        
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                        
                    j+=1
                    k-=1
                    
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    k-=1
        return res