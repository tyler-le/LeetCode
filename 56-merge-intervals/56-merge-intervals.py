class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda i : i[0])
        res = []
        res.append(intervals[0])
        
        for interval in intervals[1:]:
            prev_start, prev_end = res[-1]
            curr_start, curr_end = interval
            
            has_overlap = (prev_end >= curr_start and prev_end <= curr_end) or (prev_start <= curr_end <= prev_end)
            print(has_overlap)
            if has_overlap:
                res[-1] = [min(prev_start, curr_start), max(prev_end, curr_end)]
            else:
                res.append(interval)
                
        return res