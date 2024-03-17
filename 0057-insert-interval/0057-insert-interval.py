class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            
            # case 1 - new interval comes before most previous
            if newInterval[1] < curr_start:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            
            # new interval comes after most previous
            elif curr_end < newInterval[0] :
                res.append(intervals[i])
                
            
            # new interval overlaps with most previous
            else:
                newInterval = [min(curr_start, newInterval[0]), max(curr_end, newInterval[1])]
        
        res.append(newInterval)
        
        return res