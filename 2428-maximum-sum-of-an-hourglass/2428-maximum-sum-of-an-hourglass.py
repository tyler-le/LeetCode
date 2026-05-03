class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row_sums = defaultdict(list)

        n = len(grid)
        m = len(grid[0])
        res = -math.inf

        for i in range(n):
            for j in range(m):

                # calc row prefix sum
                row_prefix = row_sums[i]
                if not row_prefix:
                    row_prefix.append(grid[i][j])
                else: 
                    row_prefix.append(grid[i][j] + row_prefix[-1])
        
        for i in range(n-2):
            for j in range(m-2):
                top_horizontal = row_sums[i][j+2] - (row_sums[i][j-1] if j - 1 >= 0 else 0)
                bottom_horizontal = row_sums[i+2][j+2] - (row_sums[i+2][j-1] if j - 1 >= 0 else 0)
                middle = grid[i+1][j+1]
                res = max(res, top_horizontal + bottom_horizontal + middle)
        
        return res






                