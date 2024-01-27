class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if not intervals: return True
        
        intervals.sort(key = lambda x : x[0])
        
        prev_start, prev_end = intervals[0]
        
        for curr_start, curr_end in intervals[1:]:
            if prev_start <= curr_start < prev_end: return False
            prev_start, prev_end = curr_start, curr_end
        
        return True
            