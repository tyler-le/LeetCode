class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : x[0])
        min_heap = [intervals[0][1]]

        for curr_start, curr_end in intervals[1:]:
            if curr_start < min_heap[0]:
                heappush(min_heap, curr_end)
            else:
                heappush(min_heap, max(heappop(min_heap), curr_end))
        
        return len(min_heap)
        
