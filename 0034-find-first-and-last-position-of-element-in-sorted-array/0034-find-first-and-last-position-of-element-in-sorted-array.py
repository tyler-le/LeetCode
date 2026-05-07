class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums: return [-1, -1]
        n = len(nums)
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)


        if left == n or right - 1 == n or nums[left]!=target or nums[right-1] != target:
            return [-1, -1]
        return [left, right - 1]
