class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        def rec(left, right):
            
            # base case
            if left >= right: return 0
            
            # calculate area
            w, h = right - left, min(height[left], height[right])
            area = w * h

            # recursive call
            if height[left] < height[right]:
                return max(area, rec(left+1, right))
            else:
                 return max(area, rec(left, right-1))
                
        
        return rec(0, len(height) - 1)
