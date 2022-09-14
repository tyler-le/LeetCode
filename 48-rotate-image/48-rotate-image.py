class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # A more fancy way is to transpose (flip across diagonal) and then to reflect (reverse).
        # This is the same as rotating it
        
        rows = cols = len(matrix)
        
        def transpose():
            
            for r in range(rows):
                for c in range(r+1, cols):
                    matrix[r][c], matrix[c][r] = matrix [c][r], matrix[r][c]
        
        def reflect():
            for row in matrix:
                row = row.reverse()
        
        transpose()
        reflect()
