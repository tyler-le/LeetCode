class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        # greedy + heap
        # remove lowest counts first
        
        cnt = list(Counter(arr).values())
        heapify(cnt)
        
        for _ in range(k):
            popped = heappop(cnt)
            if popped > 1:
                heappush(cnt, popped-1)
                
        return len(cnt)