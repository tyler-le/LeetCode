class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # [-1, 0, 1, 2, -1, -4]
        #   ^
        #   i
        
        # check for a PAIR where pair = 0 - nums[i] 
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            curr = nums[i]
            
            left = i+1
            right = len(nums)-1
            while(left < right):
                
                if nums[left] + nums[right] + curr == 0:
                    res.append([curr, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
                elif nums[left] + nums[right] + curr < 0:
                    left+=1
                else:
                    right-=1
                    
        return res