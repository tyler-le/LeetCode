class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # [1, 3, 3, 3, 4]
        
        nums.sort()
        res = 0
        l, r = 0, len(nums)-1
        
        while l < r:
            if nums[l] + nums[r] == k:
                res+=1
                l+=1
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                r-=1
        return res