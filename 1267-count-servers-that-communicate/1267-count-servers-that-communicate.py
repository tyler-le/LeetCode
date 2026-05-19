class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        row_cnt = defaultdict(int)
        col_cnt = defaultdict(int)

        n, m = len(grid), len(grid[0])
        res = 0
        first = None

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                row_cnt[i]+=1
                col_cnt[j]+=1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                if row_cnt[i] == 1 and col_cnt[j] == 1: continue
                res+=1
        
        return res