class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0])
        
        print(intervals)
        for i in range(1, len(intervals)):
            start1, end1 = intervals[i-1]
            start2, end2 = intervals[i]
            
            has_overlap = (start1 <= start2 < end1)
            if has_overlap: return False
        return True
            