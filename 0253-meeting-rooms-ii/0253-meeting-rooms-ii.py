class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x : x[0])
        min_heap = []

        # keep track of the occupied rooms via their end times
        # store these end times in a min heap
        # min heap because we want access to the room that ends first
        # check if we can book. if not, add a new room, otherwise extend that rooms booking time

        for start, end in intervals:
            if not min_heap or start < min_heap[0]:
                # add a new room
                heappush(min_heap, end)
            else:
                # extend the room booking
                heappop(min_heap)
                heappush(min_heap, end)
        
        return len(min_heap)

