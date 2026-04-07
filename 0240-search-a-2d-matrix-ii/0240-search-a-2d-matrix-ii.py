class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        """
        Iterative version of the recursive approach
        """
        i, j = 0, m-1

        while i < n and j >= 0:
            top_right = matrix[i][j]
            if top_right > target: j-=1
            elif top_right < target: i+=1
            else: return True
        
        return False

        """
        The idea is to look at the top right corner.
        Compare top right corner with the target
        We can easily eliminate a single row or column with this comparison
        """

        # f(i, j) = target exists within top right corner (i,j) to bottom left
        def f(i, j):
            if i == n or j < 0: return False

            top_right = matrix[i][j]

            if top_right > target: return f(i, j-1)
            elif top_right < target: return f(i+1, j)
            else: return True


        
        return f(0, m-1)
