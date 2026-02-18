class Solution:
    def reorganizeString(self, s: str) -> str:
        res, cnt = [], Counter(s)
        max_heap = [(freq, ch) for ch, freq in cnt.items()]
        heapify_max(max_heap)
        prev_freq, prev_ch = None, None
        
        while max_heap:
            curr_freq, curr_ch = heappop_max(max_heap)
            # if res and curr_ch == res[-1]: return ""
            res.append(curr_ch)
            if prev_ch and prev_freq > 1: 
                heappush_max(max_heap, (prev_freq - 1, prev_ch))
            prev_freq, prev_ch = curr_freq, curr_ch
        
        return "".join(res) if len(res) == len(s) else ""
