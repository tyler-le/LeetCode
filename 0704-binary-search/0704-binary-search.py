class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums, target, 0, len(nums))
        if 0 <= index < len(nums) and target == nums[index]: return index
        return -1
        