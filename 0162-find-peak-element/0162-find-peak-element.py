class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        low, high = 0, n - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            before = nums[mid-1] if mid - 1 >= 0 else -math.inf
            after = nums[mid+1] if mid + 1 < n else -math.inf
            curr = nums[mid]

            if before < curr and curr > after: 
                return mid
            
            elif before <= curr:
                low = mid + 1
            
            else:
                high = mid - 1