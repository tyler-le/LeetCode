class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # -------------------------------------------------[0,30]
        #      ------------ [5,10]
        #                             ------ [15,20]

        # # sort by start

        # [[0,30],[5,10],[15,20]]

        # data structure min heap - keep track of each rooms end time
        # [20, 30]


        intervals.sort(key = lambda x : x[0])
        min_heap = [] # end times
        n = len(intervals)

        for i in range(n):
            curr_start, curr_end = intervals[i]

            if not min_heap:
                heappush(min_heap, curr_end)
            else:
                # merge with the best room
                if min_heap[0] <= curr_start:
                    heappop(min_heap)
                    heappush(min_heap, curr_end)

                # create a new room
                else:
                    heappush(min_heap, curr_end)

        return len(min_heap)



        