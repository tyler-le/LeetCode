class Solution:
    def _has_overlap(self, x, y):
        x_start, x_end = x
        y_start, y_end = y
        return x_start <= y_start <= x_end or y_start <= x_start <= y_end

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]

            # case 1 - newInterval comes before curr_interval
            if newInterval[1] < curr_start:
                # append newInterval + rest of array
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # case 2 - newInterval comes after curr_interval
            elif newInterval[0] > curr_end:
                # append curr_interval
                res.append(intervals[i])

            # case 3 - newInterval conflicts with curr_interval
            else:
                # merge and continue
                newInterval = [min(newInterval[0], curr_start), max(newInterval[1], curr_end)]

        res.append(newInterval)
        return res
            
