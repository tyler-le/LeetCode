from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        backlog = deque()
        s = []  

        max_heap = []
        if a: max_heap.append((a, "a"))
        if b: max_heap.append((b, "b"))
        if c: max_heap.append((c, "c"))
        heapify_max(max_heap)
        

        while max_heap:
            prev = s[-1] if len(s) >= 1 else None
            prev_prev = s[-2] if len(s) >= 2 else None

            popped_freq, popped_ch = heappop_max(max_heap)

            if popped_ch == prev == prev_prev:
                backlog.append((popped_freq, popped_ch))
                continue
            
            else:
                s.append(popped_ch)
                if popped_freq - 1 > 0:
                    heappush_max(max_heap, (popped_freq - 1, popped_ch))

            if backlog:
                heappush_max(max_heap, backlog.popleft())
            
        return "".join(s)
           