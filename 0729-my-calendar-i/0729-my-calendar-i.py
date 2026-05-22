class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, startTime: int, endTime: int) -> bool:
    
        if not self.intervals: 
            self.intervals.append([startTime, endTime])
            return True

        low, high = 0, len(self.intervals)

        while low < high:
            mid = low + ((high - low) // 2)

            # compare (start, end) with self.intervals[mid] 
            mid_start, mid_end = self.intervals[mid]

            if startTime >= mid_end:
                low = mid + 1
            elif endTime <= mid_start:
                high = mid 
            else:
                return False

            
        if low == 0:
            # compare with first interval
            first_start, first_end = self.intervals[0]
            if endTime <= first_start: 
                self.intervals.insert(low, [startTime, endTime])
                return True


        elif low == len(self.intervals):
            # compare with last interval
            last_start, last_end = self.intervals[-1]
            if last_end <= startTime:
                self.intervals.append([startTime, endTime])
                return True
        else:
            # compare with adjacent intervals
            prev_start, prev_end = self.intervals[low-1]
            after_start, after_end = self.intervals[low]

            if prev_end <= startTime and endTime <= after_start:
                self.intervals.insert(low, [startTime, endTime])
                return True

        return False
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)