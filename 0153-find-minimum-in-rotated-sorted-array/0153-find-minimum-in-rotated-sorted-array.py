# THIS IS A GOOD SOL. DO NOT DELETE

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(lo, hi):
            mid = lo + (hi - lo) // 2
            
            # base case: list is sorted
            if (nums[lo] < nums[mid] < nums[hi]):
                return nums[lo]
            
            # base case: list has 1 or 2 elems
            if hi - lo + 1 <= 2:
                return min(nums[lo], nums[hi])
            
            # recursive call. 
            # search part where nums[lo] is greater than nums[hi], 
            # indicating the pivot
            if nums[lo] < nums[mid]:
                return binary_search(mid+1, hi)
            else:
                return binary_search(lo, mid)

        # start the recursion
        lo, hi = 0, len(nums)-1
        return binary_search(lo, hi)
                