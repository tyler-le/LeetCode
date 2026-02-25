class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x : (x[0], x[1]))
        prev_end = intervals[0][1]
        res = 0

        for curr_start, curr_end in intervals[1:]:

            # if there is overlap - keep the one that ends earlier
            if curr_start < prev_end:
                prev_end = min(prev_end, curr_end)
                res+=1

            # else no overlap - keep this interval  
            else:
                prev_end = curr_end
                

        return res