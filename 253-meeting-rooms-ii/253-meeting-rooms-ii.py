class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Intuition: Keep a min heap of which rooms END first. 
        Use that to see if there will be a room available for a particular interval
        '''
        res = 1
        intervals.sort(key = lambda i : i[0])
        
        # min-heap based on smallest END time
        min_heap = [[intervals[0][1], intervals[0][0]]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # note that start, end are switched
            min_end, min_start = min_heap[0]
            
            # we can use this room
            if min_end <= start: 
                heappop(min_heap)
                heappush(min_heap, [end, start])
                
            # else create a new room
            else:
                res+=1
                heappush(min_heap, [end, start])
        
        return res
            
        