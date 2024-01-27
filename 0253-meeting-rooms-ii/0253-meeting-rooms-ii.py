class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort(key = lambda x : x[0])
        res = 0
        min_heap = [intervals[0][1]]
        
        for curr_start, curr_end in intervals[1:]:
            prev_end = min_heap[0] 
            if prev_end<=curr_start: heappop(min_heap)
            else: res+=1
                
            heappush(min_heap, curr_end)
            
        return len(min_heap)
            
        