class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            
            # mid is on left side of mountain
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            # mid is on the right side of the mountain
            elif arr[mid] > arr[mid + 1]:
                high = mid - 1
                
        return low
                
        