class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        start, end  = 0, 1
        res = []
        
        for i in range (len(intervals)):
            # w/ respect to newInterval
            comes_before = newInterval[end] < intervals[i][start]
            comes_after = newInterval[start] > intervals[i][end]
            
            if comes_before: 
                res.append(newInterval)
                res+=intervals[i:]
                return res
            
            elif comes_after: 
                res.append(intervals[i])
                
            else:
                newInterval = [min(newInterval[start], intervals[i][start]), \
                               max(newInterval[end], intervals[i][end])]
                
        res.append(newInterval)
        return res