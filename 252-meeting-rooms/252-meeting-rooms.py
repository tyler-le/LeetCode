class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key = lambda i : i[0])
        
        start, end = 0, 1
        
        for i in range(1, len(intervals)):
            has_overlap = intervals[i][start] >= intervals[i-1][start] \
                            and intervals[i][start] < intervals[i-1][end]
            
            if has_overlap: return False
            
        return True