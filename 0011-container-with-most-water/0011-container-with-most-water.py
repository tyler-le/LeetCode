class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            length = r-l
            h = min(height[l], height[r])
            area = length * h
            res = max(res, area)
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return res