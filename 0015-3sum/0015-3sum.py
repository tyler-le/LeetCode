class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()


        # [-4, -1, -1, 0, 1, 3]

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]: 
                continue

            l, r = i+1, n-1

            target = -nums[i]

            while l < r:
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l > 0 and l < n and nums[l] == nums[l-1]: 
                        l+=1
                    while r >= 0 and r < n - 1 and nums[r] == nums[r+1]: 
                        r-=1
        
        return res



            

        return res