class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda i : i[0])
        
        res = []
        res.append(intervals[0])
        
        for start,end in intervals[1:]:
            last_in_res = res[-1]
            a_overlaps_b = start>=last_in_res[0] and start <=last_in_res[1]
            b_overlaps_a = last_in_res[0]>=start and last_in_res[0]<=end
            
            if a_overlaps_b or b_overlaps_a:
                res[-1] = [min(start, last_in_res[0]), max(end, last_in_res[1])]
                
            else:
                res.append([start,end])

        return res
        