class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # min-heap => (freq, val)
        
        cnt = Counter(arr)
        min_heap = [(v,k) for (k,v) in cnt.items()]
        heapify(min_heap)
        
        for _ in range(k):
            popped_freq, popped_val = heappop(min_heap)
            
            if popped_freq > 1:
                heappush(min_heap, (popped_freq-1, popped_val))
        
        return len(min_heap)