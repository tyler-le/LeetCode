class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = res[-1]
            
            has_overlap = prev_start <= curr_start <= prev_end
            
            # has overlap, merge smallest start, largest end
            if has_overlap:
                res[-1] = [min(prev_start, curr_start), max(prev_end, curr_end)]
            
            # does not have overlap, append to res
            else:
                res.append([curr_start, curr_end])
                
        return res
        