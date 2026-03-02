class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 0. sort by start time
        # 1. check overlap
        # 2. if not overlap -> insert current interval
        # 3. if overlap -> new interval is the min starts and max ends
        # 4. add new interval to list

        res = []
        n = len(intervals)

        for i in range(n):
            curr_start, curr_end = intervals[i]

            # new_interval comes before curr_interval
            if newInterval[1] < curr_start:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # new_interval comes after curr_interval
            elif newInterval[0] > curr_end:
                res.append(intervals[i])

            # new_interval overlaps with curr_interval
            else:
                newInterval = [min(curr_start, newInterval[0]), max(curr_end, newInterval[1])]
        
        res.append(newInterval)
        return res


