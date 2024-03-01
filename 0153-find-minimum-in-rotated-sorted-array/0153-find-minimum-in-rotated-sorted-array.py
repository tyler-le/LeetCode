class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + ((high - low) // 2)
            
            # check if right side is sorted
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
            
            
        return nums[high]