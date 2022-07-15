class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0, 1
        
        # get intervals
        interval_map = {}
        for i in range(len(s)):
            if s[i] in interval_map:
                interval_map[s[i]][end] = i
            else:
                interval_map[s[i]] = [i,i]
                
        # turn map into list 
        intervals = list(interval_map.values())
        
        # merge intervals
        merged_intervals = []
        merged_intervals.append(intervals[0])
        for interval in intervals[1:]:
            has_overlap = interval[start] >= merged_intervals[-1][start] and interval[start] <= merged_intervals[-1][end]
            
            if has_overlap:
                merged_intervals[-1] = [min(interval[start], merged_intervals[-1][start]), max(interval[end], merged_intervals[-1][end])]
                
            else:
                merged_intervals.append(interval)
                
        # now we need the ranges of each interval
        res = []
        for left, right in merged_intervals:
            res.append(right - left + 1)
            
        return res
        
        
        