class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # binary search to find pivot
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
            if nums[mid] == target:
                return mid
            
            elif nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
        