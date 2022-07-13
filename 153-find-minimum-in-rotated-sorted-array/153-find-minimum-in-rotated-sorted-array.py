class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        
        while l<=r:
            mid = l + ((r-l)//2)
            
            if mid > l and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            elif mid < r and nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            if nums[l] < nums[mid]:
                l = mid+1
            else:
                r = mid - 1
                            
        return nums[0]
            