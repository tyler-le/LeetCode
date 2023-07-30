class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = collections.defaultdict(int)
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n : return 0
            if row == m-1 and col == n-1: return 1
            
            if (row,col) in dp: return dp[(row,col)]
            dp[(row,col)] = dfs(row+1, col) + dfs(row, col+1)
            return dp[(row, col)]
        
        return dfs(0,0)
        
        