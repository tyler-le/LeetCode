class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        def rec(numRows):
            if numRows == 0: return []
            if numRows == 1: return [[1]]
            
            prev_rows = rec(numRows - 1)
            curr_row = []

            for i in range(1, len(prev_rows)):
                curr_row.append(prev_rows[-1][i-1] + prev_rows[-1][i])
            
            prev_rows.append([1] + curr_row + [1])
            return prev_rows
        
        
        return rec(numRows)
            