class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        prev_start, prev_end = intervals[0]

        for curr_start, curr_end in intervals[1:]:
            # if they overlap, merge them
            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)

            # if they don't overlap, add prev to res, set prev to curr
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = curr_start, curr_end
        
        # add the last interval in
        res.append([prev_start, prev_end])
        return res