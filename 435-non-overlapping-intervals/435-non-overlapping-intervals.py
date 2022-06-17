class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res, prev_end = 0, intervals[0][1]
        
        for start,end in intervals[1:]:
            has_overlap = start < prev_end
            
            if has_overlap:
                res+=1
                prev_end = min(end, prev_end)
            else:
                prev_end = max(prev_end, end)
                
        return res
        