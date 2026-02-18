class Solution:
    def reorganizeString(self, s: str) -> str:

        max_heap = [(freq, ch) for ch, freq in Counter(s).items()] # (freq, ch)
        heapify_max(max_heap)
        res = []
        prev_ch, prev_freq = None, None

        while max_heap:
            # process curr
            popped_freq, popped_ch = heappop_max(max_heap)
            # if res and res[-1] == popped_ch: return ""

            res.append(popped_ch)

            # put prev back in
            if prev_ch and prev_freq > 1:
                heappush_max(max_heap, (prev_freq - 1, prev_ch))

            # set prev
            prev_ch, prev_freq = popped_ch, popped_freq
        
        return "".join(res) if len(res) == len(s) else ""