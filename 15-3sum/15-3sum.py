class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            target = 0-nums[i]
            j, k = i+1, len(nums)-1
            while j < len(nums) and k >= 0 and j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    print(i,j,k)
                    while j+1 < len(nums) and nums[j+1] == nums[j]: 
                        j+=1
                    while k-1 >= 0 and nums[k-1] == nums[k]: 
                        k-=1
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < target: j+=1
                else: k-=1

                
            
        return res
                            
                            
            
            
        