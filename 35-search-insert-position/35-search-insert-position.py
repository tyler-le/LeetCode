class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def modified_binary_search(nums, target, low, high):
        
            mid = low + ( (high - low) / 2)
            print (mid)
            if low > high:
                if target > nums[len(nums) - 1]:
                    return len(nums)
                elif target < nums[0]:
                    return 0
                else:
                    return mid+1
            
            if nums[mid] < target:
                return modified_binary_search(nums, target, mid+1, high)
            elif nums[mid] > target:
                return modified_binary_search(nums, target, low, mid-1)
            else:
                return mid
            
        return modified_binary_search(nums, target, 0, len(nums)-1)
        