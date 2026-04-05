"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        count = 0
        events = [] # (time, +/- employee)
        intervals = []
        res = []
        last_time = None


        for sublist in schedule:
            for interval in sublist:
                intervals.append(interval)

            
        for interval in intervals:
            start, end = interval.start, interval.end
            events.append([start, 1])
            events.append([end, -1])

        events.sort(key = lambda x : (x[0], -x[1]))

        for time, delta in events:
            count+=delta

            if not count and not last_time:
                last_time = time
                
            elif last_time:
                res.append(Interval(start=last_time, end=time))
                last_time = None
        
        return res
            

