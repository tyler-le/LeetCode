class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        max_from_left = [0 for _ in range(n)]        
        max_from_right = [0 for _ in range(n)]        
        res = 0
        
        for i in range(n):
            if i == 0: max_from_left[0] = height[0]
            else: max_from_left[i] = max(max_from_left[i-1], height[i])
    
        for i in range(n-1, -1, -1):
            if i == n-1: max_from_right[n-1] = height[n-1]
            else: max_from_right[i] = max(max_from_right[i+1], height[i])
                
        for i in range(n):
            h = min(max_from_right[i], max_from_left[i])
            res+=(h - height[i])
        
        return res
            