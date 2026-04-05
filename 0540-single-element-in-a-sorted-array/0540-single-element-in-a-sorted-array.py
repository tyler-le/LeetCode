class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1

        while low < high:
            mid = (high + low) // 2

            print(mid)

            # if mid is even, the duplicate SHOULD be on the right
            if not mid % 2:
                if mid + 1 < n and nums[mid] == nums[mid + 1]:
                    low = mid + 1
                else:
                    high = mid
            
            # if mid is odd, the duplicate should be on the left
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid

        return nums[low]

