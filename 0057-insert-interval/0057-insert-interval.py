class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        def rec(i):
            nonlocal newInterval, res
            
            # Base case: when all intervals are processed
            if i == len(intervals):
                res.append(newInterval)
                return
            
            # newInterval comes before intervals[index]
            if newInterval[1] < intervals[i][0]:
                res+=[newInterval]
                res.extend(intervals[i:])
                return 
            
            # newInterval comes after intervals[index]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                rec(i+1)
            
            # newInterval conflicts with intervals[index]
            else:
                mn = min(newInterval[0], intervals[i][0])
                mx = max(newInterval[1], intervals[i][1])
                newInterval = [mn, mx]
                rec(i+1)
            
        rec(0)
        return res
    
    