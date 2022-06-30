class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(nums, target, low, high):
            
            while low <= high:
                mid = low + ( (high - low) // 2)
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
                
            return -1
            
            
            
            
        valley_index = len(nums) - 1
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                valley_index = i+1
                break
                
        left = binary_search(nums, target, 0, valley_index - 1)
        right = binary_search(nums, target, valley_index, len(nums) - 1)
        
        if left == -1 and right == -1:
            return -1
        elif left == -1:
            return right
        else:
            return left
        
        
            
        