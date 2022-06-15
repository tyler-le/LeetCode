class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range (len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res
            
    
                
            
        return res
                
            
        