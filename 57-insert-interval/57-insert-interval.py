class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range (len(intervals)):
            # if newInterval comes before current interval and is disjoint, 
            # put it up front and attach the rest of intervals (which is nonoverlapping) and return
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            
            # else if the newInterval is not connected to curr interval, we can add the interval[i] 
            # and continue without appending
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # else there is overlap, so we update the newInterval continue without appending
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res
                            
            
        