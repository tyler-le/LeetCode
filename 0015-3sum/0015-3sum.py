class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            target = -nums[i]
            l, r = i+1, n-1
            
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while (l+1 < n) and nums[l+1] == nums[l]: l+=1
                    while (r-1 >= 0) and nums[r-1] == nums[r]: r-=1
                    l+=1
                    r-=1
                    
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    r-=1
        return res
            
        
            