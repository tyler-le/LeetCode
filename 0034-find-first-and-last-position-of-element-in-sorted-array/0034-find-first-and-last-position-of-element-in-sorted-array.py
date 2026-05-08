class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums: return [-1, -1]
        n = len(nums)
        left_bound, right_bound = -1, -1
        

        
        
        # find left bound
        low, high = 0, n-1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                left_bound = mid
                high = mid - 1

        
        # find right bound
        low, high = 0, n-1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                right_bound = mid
                low = mid + 1


        if left_bound == -1 or right_bound == -1:
            return [-1, -1]
        else:
            return [left_bound, right_bound]

