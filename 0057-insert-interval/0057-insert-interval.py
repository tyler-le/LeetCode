class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        if not intervals: return [newInterval]
        
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            
            # case 1 - new interval comes before most previous
            if newInterval[1] < curr_start:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            
            # case 2 - new interval comes after curr interval
            elif curr_end < newInterval[0] :
                res.append(intervals[i])
                
            
            # case 3 - new interval overlaps with most previous
            else:
                newInterval = [min(curr_start, newInterval[0]), max(curr_end, newInterval[1])]
            
        # for cases 2 and 3, where we never added the new interval to the result
        res.append(newInterval)
        
        return res