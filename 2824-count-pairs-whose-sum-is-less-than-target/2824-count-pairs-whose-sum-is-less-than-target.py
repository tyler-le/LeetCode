class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, len(nums)-1
        
        while l < r:
            sumi = nums[l] + nums[r]
            if sumi < target:
                res+= (r - l)
                l+=1
            else:
                r-=1
        return res