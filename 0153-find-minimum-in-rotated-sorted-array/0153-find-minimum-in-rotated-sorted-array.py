class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        
        while low < high:
            mid = low + ((high - low) // 2)
            if mid+1 < n and nums[mid] > nums[mid+1]: return nums[mid+1]
            if mid-1 >= 0 and nums[mid] < nums[mid-1]: return nums[mid]
            
            if nums[low] < nums[mid]: low = mid + 1
            else: high = mid - 1
                
        return nums[0]