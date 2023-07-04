class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
            
            
            
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target: 
                return mid
            
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
     
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
                
        return -1
                