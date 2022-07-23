class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l < r:
                curr_sum = sum((nums[i], nums[l], nums[r]))
                if curr_sum < target:
                    res += r-l
                    l+=1
                else:
                    r-=1
            
            
        return res