class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [] # (location, +/- passengers)

        for passengers, src, dst in trips:
            events.append((src, passengers))
            events.append((dst, -passengers))
        
        events.sort(key = lambda x : (x[0], x[1]) )
        curr_capacity = 0

        for _, delta in events:
            curr_capacity+=delta
            if curr_capacity > capacity: return False
        
        return True