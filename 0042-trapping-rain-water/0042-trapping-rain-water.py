class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        max_from_left = [0 for _ in range(n)]        
        max_from_right = [0 for _ in range(n)]
        
        max_from_left[0] = height[0]
        max_from_right[-1] = height[-1]
        
        res = 0
        
        for i in range(1, n):
            max_from_left[i] = max(max_from_left[i-1], height[i])
            
        for i in range(n-2, -1, -1):
            max_from_right[i] = max(max_from_right[i+1], height[i])
            
        for i in range(1, n):
            res += min(max_from_left[i], max_from_right[i]) - height[i]
            
        return res