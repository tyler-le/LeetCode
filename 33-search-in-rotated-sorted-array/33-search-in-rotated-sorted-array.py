class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
            if nums[mid] == target: return mid
            
            # low to mid portion is sorted
            elif nums[low] <= nums[mid]:
                # adjust ranges accordingly
                if nums[low] <= target < nums[mid]: high = mid - 1
                else: low = mid + 1
                
            # mid to high portion is sorted
            elif nums[mid] <= nums[high]:
                # adjust ranges accordingly
                if nums[mid] < target <= nums[high]: low = mid + 1
                else: high = mid - 1
                
        return -1
            
            
        
        