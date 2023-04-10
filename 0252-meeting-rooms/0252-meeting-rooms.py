class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals: return True
        
        intervals.sort(key = lambda x : x[1])
        curr_start, curr_end = intervals[0]
        
        for next_start, next_end in intervals[1:]:
            if next_start < curr_end <= next_end:
                return False
            curr_start, curr_end = next_start, next_end
            
        return True