class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        lo, high = 0, n-1
        
        while lo <= high:
            mid = (high+lo) // 2
    
            # check increasing -> search right
            if arr[mid] < arr[mid+1]:
                lo = mid + 1

            # check decreasing -> search left
            elif arr[mid] > arr[mid + 1]:
                high = mid - 1
                
        return lo