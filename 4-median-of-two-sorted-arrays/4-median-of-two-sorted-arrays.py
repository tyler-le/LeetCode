class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        
        nums.sort()
        
        l, r = 0, len(nums)-1
        
        while l < r:
            l+=1
            r-=1
        
        median = nums[r] if (l == r) else (nums[l] + nums[r]) / 2.0
            
        return median