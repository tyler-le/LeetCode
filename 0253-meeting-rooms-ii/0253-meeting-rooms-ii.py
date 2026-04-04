class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : x[0])
        min_heap = []

        for start, end in intervals:
            if not min_heap:
                heappush(min_heap, end)
            elif start < min_heap[0]:
                heappush(min_heap, end)
            else:
                heappop(min_heap)
                heappush(min_heap, end)
        
        return len(min_heap)

        # keep track of the earliest end time