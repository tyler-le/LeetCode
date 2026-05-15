class Solution:
    def trap(self, height: List[int]) -> int:
        tallest_from_left = []
        tallest_from_right = []
        n = len(height)
        res = 0

        for i in range(n):
            if not tallest_from_left: tallest_from_left.append(height[i])
            else: tallest_from_left.append(max(height[i], tallest_from_left[i-1]))
        
        for i in range(n-1, -1, -1):
            if not tallest_from_right: tallest_from_right.append(height[i])
            else: tallest_from_right.append(max(height[i], tallest_from_right[-1]))

        tallest_from_right.reverse()
        
        for i in range(1, n-1):
            h = height[i]
            smallest = min(tallest_from_left[i-1], tallest_from_right[i+1])
            res+=(max(0, smallest-h))
        
        return res


        