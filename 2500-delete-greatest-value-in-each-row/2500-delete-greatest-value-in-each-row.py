class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        # for each row, delete biggest element
        # of these deleted elements, add the max to res
        
        min_heaps = []
        res = 0
        
        for row in grid:
            min_heaps.append([-x for x in row])
            heapify(min_heaps[-1])
        
        m = len(grid[0])
        
        for _ in range(m):
            global_max = -1
            
            for min_heap in min_heaps:
                local_max = -heappop(min_heap)
                global_max = max(local_max, global_max)
            
            res+=global_max
        
        return res
                