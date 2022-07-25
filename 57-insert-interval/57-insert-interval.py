class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return [newInterval]
        
        intervals.sort(key = lambda i : i[0])
        START,END = 0,1
        res = []
        
        for i in range (len(intervals)):
            comes_before = newInterval[END] < intervals[i][START]
            comes_after = newInterval[START] > intervals[i][END]
            
            if comes_before: 
                res.append(newInterval)
                res += intervals[i:]
                return res
            
            if comes_after:
                res.append(intervals[i])
                
            else:
                newInterval = [min(newInterval[START], intervals[i][START]),
                               max(newInterval[END], intervals[i][END])]
        res.append(newInterval)        
        return res
            