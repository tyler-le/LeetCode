class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        
        res = deque()
        
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res.appendleft(nums[r] ** 2)
                r-=1
            else:
                res.appendleft(nums[l] ** 2)
                l+=1
        return res