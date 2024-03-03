class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        res = deque()
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.appendleft(nums[left]**2)
                left+=1
            else:
                res.appendleft(nums[right]**2)
                right-=1
        
        return list(res)
            