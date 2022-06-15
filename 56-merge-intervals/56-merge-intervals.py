class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # custom sort based on first element in each sub-array
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        
        for start,end in intervals[1:]:
            last_in_output = output[-1]

            if last_in_output[1] >= start:
                if last_in_output[1] <= end:
                    last_in_output[1] = end
                    
                
            else:
                output.append([start,end])
                
        return output
        