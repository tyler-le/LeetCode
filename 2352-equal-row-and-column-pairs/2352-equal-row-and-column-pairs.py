class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        rows_map = defaultdict(int)
        cols = [[] for _ in range (m)]
        
        for row in grid:
            rows_map[tuple(row)]+=1
        
        for i in range(n):
            for j in range(m):
                cols[j].append(grid[i][j])
        
        res = 0

        for col in cols:
            res+=rows_map[tuple(col)]
        
        return res

