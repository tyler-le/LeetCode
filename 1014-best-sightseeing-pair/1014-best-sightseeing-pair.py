class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # score = values[i] + values[j] + i − j
        #       = (values[i] + i) + (values[j] - j) (maximize)
        #       = maximize (values[i] + i) + maximize (values[j] - j)
                
                # algo - keep track of the max (values[i] + i) seen so far
                # use that to keep track of the max score
                
                max_potential = values[0] + 0
                n = len(values)
                res = 0
                
                for j in range(1, n):
                    res = max(res, max_potential + values[j] - j)
                    curr_potential = values[j] + j
                    max_potential = max(max_potential, curr_potential)
                    
                return res
                    
                    
                
                