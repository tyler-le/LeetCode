class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # count the min number of meeting rooms required
        # keep track of the room that ends first (min heap end time)
        # if we cannot reserve a room for that one, 
        # then we cannot reserve a room for any of them

        intervals.sort(key = lambda x : x[0])
        min_heap = [intervals[0][1]]

        for curr_start, curr_end in intervals[1:]:
            
            top = min_heap[0]
            if curr_start < top:
                heappush(min_heap, curr_end)
            else:
                heappop(min_heap)
                heappush(min_heap, curr_end)
        
        print(min_heap)
        return len(min_heap)
