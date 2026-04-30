class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        n, m = len(heights), len(heights[0])

        def dfs(x, y, reachable):
            
            if (x,y) in reachable: return
            reachable.add((x,y))

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:

                r = x + dx
                c = y + dy

                if r < 0 or c < 0 or r >= n or c >= m: continue
                if heights[x][y] > heights[r][c]: continue
                
                dfs(r, c, reachable)



        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m-1, atlantic)

        for j in range(m):
            dfs(0, j, pacific)
            dfs(n-1, j, atlantic)

        return list(atlantic & pacific)