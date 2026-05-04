class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])
        prefix_sum = [[0 for _ in range(m)] for _ in range(n)]
        res = [[0 for _ in range(m)] for _ in range(n)]
        

        for i in range(n):
            acc = 0
            for j in range(m):
                acc+=mat[i][j]
                prefix_sum[i][j] = acc + (prefix_sum[i-1][j] or 0)
        
        for i in range(n):
            for j in range(m):
                top_row = max(0, i-k)
                bottom_row = min(n-1, i+k)
                left_col = max(0, j-k)
                right_col = min(m-1, j+k)

                total = prefix_sum[bottom_row][right_col]
                top = prefix_sum[top_row-1][right_col] if top_row - 1 >= 0 else 0
                left = prefix_sum[bottom_row][left_col-1] if left_col - 1 >= 0 else 0
                corner = prefix_sum[top_row-1][left_col-1] if (top_row - 1 >= 0 and left_col - 1 >= 0) else 0
                res[i][j] =  total - top - left + corner
        
        return res



