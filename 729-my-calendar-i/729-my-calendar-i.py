class MyCalendar:

    def __init__(self):
        self.intervals = []
        
    
    def book(self, start: int, end: int) -> bool:

        # if overlapping intervals, early exit
        for s, e in self.intervals:
            if (start >= s and start < e) or (s >= start and s < end): 
                return False
            
        # if we get through entire calendar w/out conflicts, we can append
        self.intervals.append([start, end])
        return True
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)