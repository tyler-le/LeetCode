class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = []
        cnt = Counter(s)
        prev = []
        
        max_heap = [(-freq, ch) for ch,freq in cnt.items()]
        heapify(max_heap)
        
        while max_heap:
            curr_freq, curr_ch = heappop(max_heap)
            res.append(curr_ch)
            
            if prev and prev[0] < 0: heappush(max_heap, tuple(prev))
            
            prev = [curr_freq + 1, curr_ch]
            
        return "".join(res) if len(res) == len(s) else ""
            
            
        