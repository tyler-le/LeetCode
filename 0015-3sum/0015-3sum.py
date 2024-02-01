class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, n-1
            target = -nums[i]
            
            while l < r:
                
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l+1 < n and nums[l] == nums[l+1]: l+=1
                    while r > 0 and nums[r] == nums[r-1]: r-=1
                    l+=1
                    r-=1
                        
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    r-=1
        return res
                    