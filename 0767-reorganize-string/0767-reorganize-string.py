class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        max_heap = [(-freq, ch) for ch, freq in cnt.items()]
        heapify(max_heap)
        res = []
        prev_freq, prev_ch = 0, ""
        
        while max_heap:
            popped_freq, popped_ch = heappop(max_heap)
            popped_freq +=1
            
            if res and res[-1] == popped_ch: return ""
            
            res.append(popped_ch)
            if prev_freq != 0: heappush(max_heap, (prev_freq, prev_ch))
            
            prev_freq, prev_ch = popped_freq, popped_ch
        
        return "".join(res) if len(res) == len(s) else ""