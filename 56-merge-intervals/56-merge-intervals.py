class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i : i[0])
        
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            has_overlap = start >= res[-1][0] and start <= res[-1][1]
            
            if has_overlap:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
            
            else:
                res.append([start, end])
        
        return res