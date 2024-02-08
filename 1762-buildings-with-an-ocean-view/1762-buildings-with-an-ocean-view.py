class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curr_max = 0
        res = []
        n = len(heights)
        for i in range(n-1, -1, -1):
            height = heights[i]
            
            if height > curr_max:
                curr_max = height
                res.append(i)
                
        return res[::-1]