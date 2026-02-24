class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            left, right = i + 1, n - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left+=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]: left+=1
                    while left < right and nums[right] == nums[right+1]: right-=1
        
        return res