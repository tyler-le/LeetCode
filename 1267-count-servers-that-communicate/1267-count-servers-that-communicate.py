class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        res = 0
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i]+=1
                    cols[j]+=1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (rows[i] >= 2 or cols[j] >= 2):
                    res+=1

        return res