class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] == target: 
                return mid

            # left sorted
            if nums[low] <= nums[mid]:
                # if item exists on left
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


            # right sorted
            else:
                # if item exists on right
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1


        return -1
