class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start,end=0,1
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        
        for i in range (1, len(intervals)):
            has_overlap = (res[-1][start]>=intervals[i][start] and res[-1][start]<=intervals[i][end]) or (intervals[i][start]>=res[-1][start] and intervals[i][start]<=res[-1][end])
            
            if has_overlap:
                res[-1][start], res[-1][end] = min(res[-1][start], intervals[i][start]), max(res[-1][end], intervals[i][end])
            else:
                res.append(intervals[i])
                
        return res
        
        