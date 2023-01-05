class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end pos
        # merge intervals
        res = 1
        points.sort(key=lambda x: x[1] )
        prev_start, prev_end = points[0]
        for curr_start, curr_end in points:
                
            # does not overlap
            if curr_start > prev_end:
                prev_start, prev_end = curr_start, curr_end
                res+=1
        print(points)
        return res
