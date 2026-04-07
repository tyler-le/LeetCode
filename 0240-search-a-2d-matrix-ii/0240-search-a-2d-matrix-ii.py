class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        # f(i, j) = target exists within top right corner (i,j) to bottom left
        def f(i, j):
            print(i,j)
            if i == n or j < 0: return False

            

            top_right = matrix[i][j]

            if top_right > target: return f(i, j-1)
            elif top_right < target: return f(i+1, j)
            else: return True


        
        return f(0, m-1)
