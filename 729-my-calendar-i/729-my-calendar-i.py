class MyCalendar:

    def __init__(self):
        self.intervals = []
        
    def merge(self, intervals):
     
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        start,end = 0,1
        for interval in intervals:
            has_overlap = interval[start] <= res[-1][end] and interval[start] >= res[-1][start]
            
            if has_overlap:
                res[-1] = [min(interval[start], res[-1][start]), max(interval[end], res[-1][end])]
            else:
                res.append(interval)
                
        return res

    def book(self, start: int, end: int) -> bool:
        self.intervals.sort(key = lambda i : i[0])
        flag = True
        
        for s, e in self.intervals:
            if (start >= s and start < e) or (s >= start and s < end): 
                flag = False
                break
            
        if flag: 
            self.intervals.append([start, end])
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)