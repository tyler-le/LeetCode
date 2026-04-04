class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # be greedy and remove the one that ends later

        intervals.sort(key = lambda x : (x[0]))
        n = len(intervals)
        res = 0
        prev_start, prev_end = intervals[0]

        for i in range(1, n):
            curr_start, curr_end = intervals[i]

            has_overlap = prev_start <= curr_start < prev_end

            # if overlap: choose the one that ends earlier
            if has_overlap:
                if curr_end < prev_end:
                    prev_start, prev_end = curr_start, curr_end
                res+=1

            # else re-track prev interval
            else:
                prev_start, prev_end = curr_start, curr_end 
        
        return res