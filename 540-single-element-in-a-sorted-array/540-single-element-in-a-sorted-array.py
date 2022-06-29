class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
                
            if (mid % 2) == 0:
                if mid > 0 and nums[mid] == nums[mid-1]:
                    high = mid - 1
                elif mid < len(nums) - 1 and nums[mid] == nums[mid+1]:
                    low = mid + 1
                else:
                    return nums[mid]
            else:
                if mid > 0 and nums[mid] == nums[mid-1]:
                    low = mid + 1
                elif mid < len(nums) - 1 and nums[mid] == nums[mid+1]:
                    high = mid - 1
                else:
                    return nums[mid]
            
        
                
            