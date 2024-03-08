class Solution:
    def minDeletions(self, s: str) -> int:
        
        # max_heap
#         a - 3
#         b - 3
#         c - 2
        
#         seen_freqs [3 ]
                
        max_heap = [-freq for freq in Counter(s).values() ]
        heapify(max_heap)
        seen_freqs = set()
        res = 0
        
        for _ in range(len(max_heap)):
            popped_freq = -heappop(max_heap)
            
            while popped_freq and popped_freq in seen_freqs:
                res+=1
                popped_freq-=1
            
            if popped_freq:
                seen_freqs.add(popped_freq)
        
        return res
        
            
            