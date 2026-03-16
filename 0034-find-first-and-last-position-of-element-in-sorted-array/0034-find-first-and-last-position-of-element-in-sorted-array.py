class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        res = [-1, -1]

        if not nums: return res

        # left bound
        low, high = 0, n-1
        while low <= high:
            mid = (high + low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                # we found target, so we save it as the current left bound
                # and continue searching left for future occurrences
                res[0] = mid
                high = mid - 1

        # right bound
        low, high = 0, n-1
        while low <= high:
            mid = (high + low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                # we found target, so we save it as the current right bound
                # and continue searching right for future occurrences
                res[1] = mid
                low = mid + 1
                
        return res
        