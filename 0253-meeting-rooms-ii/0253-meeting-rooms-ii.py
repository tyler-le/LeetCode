class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # keep a min-heap of end times signifying booked rooms that end the earliest
        
        if not intervals: return 0
        
        intervals.sort(key = lambda x : x[0])
        res = 0
        min_heap = [intervals[0][1]]
        
        for curr_start, curr_end in intervals[1:]:
            prev_end = min_heap[0] 
            
            # meeting room is freed up, so curr interval can take it
            if prev_end <= curr_start: 
                heappop(min_heap)
                heappush(min_heap, curr_end)
            
            # otherwise we create a new meeting room
            else: 
                res+=1
                heappush(min_heap, curr_end)
                
        return len(min_heap)
            
        