class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1 or n == 2: return 0
        max_left, max_right = [0]*n, [0]*n
        maxL = maxR = res = 0
        
        # store max lefts in array
        for i in range(n):
            maxL = max(maxL, height[i])
            max_left[i] = maxL
          
        # store max rights in array
        for i in range(n-1, -1, -1):
            maxR = max(maxR, height[i])
            max_right[i] = maxR
            
        for i in range(1, n):
            res += min(max_left[i], max_right[i]) - height[i]
            
        return res