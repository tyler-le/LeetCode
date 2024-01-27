class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        # greedy - keep interval with smallest end time
        res = 0
        intervals.sort(key = lambda x : x[1])
        prev_end = intervals[0][1]
        
        for curr_start, curr_end in intervals[1:]:
            
            # if the two intervals overlap, keep the smaller one 
            # (since sorted, don't need to set prev_end)
            if curr_start < prev_end: 
                res+=1
            
            # else they dont overlap so update prev_end
            else: prev_end = curr_end
                
        return res
            