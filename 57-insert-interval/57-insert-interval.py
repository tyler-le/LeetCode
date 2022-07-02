class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        if len(intervals) == 0:
            return [newInterval]
        
        for i in range(len(intervals)):
            currInterval_start, currInterval_end = intervals[i][0], intervals[i][1]
            newInterval_start, newInterval_end = newInterval[0], newInterval[1]
            
            comes_before_no_overlap = newInterval_end < currInterval_start
            if comes_before_no_overlap:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            
            goes_after_no_overlap = newInterval_start > currInterval_end
            if goes_after_no_overlap:
                res.append(intervals[i])
            
            else:
                newInterval[0], newInterval[1] = min(newInterval_start, currInterval_start), max(newInterval_end, currInterval_end)
                
        res.append(newInterval)
        return res