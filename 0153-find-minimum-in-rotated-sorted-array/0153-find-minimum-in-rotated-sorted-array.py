class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        res = math.inf

        while low <= high:
            mid = low + ((high - low) // 2)

            # low to mid is sorted
            # record low as a potential min, since it's smaller
            # but search right for the inflection point
            if nums[low] <= nums[mid]:
                res = min(res, nums[low])
                low = mid + 1

            # low to mid is not sorted (nums[low] > nums[mid])
            # record nums[mid] as a potential min, since it's smaller
            # search left for the inflection point
            else:
                res = min(res, nums[mid])
                high = mid - 1

        return res

        

            