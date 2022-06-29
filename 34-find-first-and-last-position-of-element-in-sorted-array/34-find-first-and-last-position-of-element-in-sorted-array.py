class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                break
                
        if low > high:
            return [-1,-1]
        
        while nums[low] != target:
            low+=1
        while nums[high] != target:
            high-=1
        
        return [low, high]