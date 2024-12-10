# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        
        while low < high:
            mid = low + (high - low) // 2
            
            isBad = isBadVersion(mid)
            
            if isBad:
                # go lower
                high = mid
            else:
                # go higher
                low = mid + 1
                
        return high