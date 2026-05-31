class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        left_bound, right_bound = -1, -1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                left_bound = mid
                high = mid - 1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                right_bound = mid
                low = mid + 1
        
        return [left_bound, right_bound]

        
