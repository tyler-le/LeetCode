class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hmap = defaultdict(int)
        n = len(grid)
        res = 0
        
        for row in grid:
            hmap[tuple(row)]+=1
        
        for i in range(n):
            column = []
            for j in range(n):
                column.append(grid[j][i])
            column = tuple(column)
            res+=(hmap[column])
                
        return res
                
            