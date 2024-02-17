class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
        n = len(heights)
        
        for i in range(n-1):

            if heights[i] >= heights[i+1]: continue
                
            diff = heights[i+1] - heights[i]
            
            # greedily allocate a ladder
            heappush(ladder_allocations, diff)
            
            # if we've allocted too many ladders
            if len(ladder_allocations) > ladders:
                
                # convert the smallest climb ladder into a brick
                bricks-=heappop(ladder_allocations)
                
            if bricks < 0: return i
            
        return n - 1