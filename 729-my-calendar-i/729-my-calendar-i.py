class MyCalendar:

    def __init__(self):
        self.intervals = []
        
    
    def book(self, start: int, end: int) -> bool:
        #self.intervals.sort(key = lambda i : i[0])

        
        for s, e in self.intervals:
            if (start >= s and start < e) or (s >= start and s < end): 
                return False
            
        self.intervals.append([start, end])
        return True
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)