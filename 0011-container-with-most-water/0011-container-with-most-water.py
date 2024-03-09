class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        l, r = 0, n-1
        res = 0
        
        while l < r:
            width = r - l
            h = min(height[r], height[l])
            area = width * h
            
            res = max(res, area)
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return res
            
            