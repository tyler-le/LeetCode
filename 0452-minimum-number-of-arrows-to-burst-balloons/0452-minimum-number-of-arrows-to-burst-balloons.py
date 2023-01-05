class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end pos
        # interval problem
        
        points.sort(key=lambda x: x[1] )
        res, prev_end = 1, points[0][1]
        
        for curr_start, curr_end in points:
            # does not overlap
            if curr_start > prev_end:
                prev_end = curr_end
                res+=1

        return res
