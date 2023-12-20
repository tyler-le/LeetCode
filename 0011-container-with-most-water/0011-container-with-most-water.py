class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = -float('inf')
        
        while l < r:
            width = r-l
            h = min(height[l], height[r])
            area = width*h
            
            res = max(res, area)
            
            if height[l] > height[r]: r-=1
            else: l+=1
                
        return res
            