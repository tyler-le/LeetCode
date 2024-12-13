class Solution:
    def findScore(self, nums: List[int]) -> int:
        # keep a min-heap with (num, index)
        # keep a marked set
        
        n = len(nums)
        min_heap = [(nums[i], i) for i in range(n)]
        visited = set()
        heapify(min_heap)
        score = 0
        
        while len(visited) < n:
            
            popped, index = heappop(min_heap)
            if index in visited: continue
            score+=popped
            visited.add(index)
            if index > 0: visited.add(index-1)
            if index < n-1: visited.add(index+1)
                
        return score
            