class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        start,end = 0,1
        for interval in intervals:
            has_overlap = interval[start] <= res[-1][end] and interval[start] >= res[-1][start]
            
            if has_overlap:
                res[-1] = [min(interval[start], res[-1][start]), max(interval[end], res[-1][end])]
            else:
                res.append(interval)
                
        return res
        
        