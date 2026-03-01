class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [(freq, num) for num, freq in Counter(tasks).items()] # (freq, num)
        heapify_max(max_heap)
        curr_time = 0
        q = deque() # (time, freq, num)
        res = []

        while max_heap or q:
            # move from q to max heap
            while q and q[0][0] <= curr_time:
                _, popped_freq, popped_num = q.popleft()
                heappush_max(max_heap, (popped_freq, popped_num))
            
            if max_heap:
                popped_freq, popped_num = heappop_max(max_heap)
                res.append(popped_num)
                if popped_freq - 1 > 0:
                    q.append((curr_time + n + 1, popped_freq - 1, popped_num))
            else:
                res.append("idle")

            curr_time+=1
        
        return curr_time
            
            



        
        