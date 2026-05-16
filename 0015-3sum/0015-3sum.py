class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if i-1 >= 0 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = n - 1
            target = nums[i]
            while l < r:
                if nums[l] + nums[r] + nums[i] < 0: l+=1
                elif nums[l] + nums[r] + nums[i] > 0: r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < n and nums[l] == nums[l-1]: l+=1
                    while r>=0 and nums[r] == nums[r+1]: r-=1

        return res


