class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        res = []

        for i in range(len(self.intervals)):
            curr_start, curr_end = self.intervals[i]

            # [startTime, endTime] comes after [curr_start, curr_end]
            if curr_end <= startTime:
                res.append([curr_start, curr_end])


            # [startTime, endTime] comes before [curr_start, curr_end]
            elif endTime <= curr_start:
                res.append([startTime, endTime])
                res.extend(self.intervals[i:])
                self.intervals = res
                return True

            # [startTime, endTime] conflicts [curr_start, curr_end]
            else:
                return False
        
        res.append([startTime, endTime])
        self.intervals = res
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)