class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        # K: some index
        # V: next/prev smallest index for index K
        prev_smallest_elem = {}
        next_smallest_elem = {} 

        # next smallest elem
        decreasing = []
        for i in range(n):
            if not decreasing:
                decreasing.append((i, heights[i]))
                continue
            while decreasing and decreasing[-1][1] > heights[i]:
                popped_index, popped_val = decreasing.pop()
                next_smallest_elem[popped_index] = i
            decreasing.append((i, heights[i]))

        # prev smallest elem
        decreasing = []
        for i in range(n-1, -1, -1):
            if not decreasing:
                decreasing.append((i, heights[i]))
                continue
            while decreasing and decreasing[-1][1] > heights[i]:
                popped_index, popped_val = decreasing.pop()
                prev_smallest_elem[popped_index] = i
            decreasing.append((i, heights[i]))



        for i in range(n):
            left = prev_smallest_elem[i] if i in prev_smallest_elem else -1
            right = next_smallest_elem[i] if i in next_smallest_elem else n
            res = max(res, heights[i] * (right-left-1))

        
        return res