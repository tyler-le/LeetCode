class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        max_heap = [[-count, char] for char, count in count.items()]
        heapify(max_heap)
        
        res = []
        prev = []
        
        while max_heap:
            popped = heappop(max_heap)
            curr_freq, curr_letter  = popped[0], popped[1]
            res += [curr_letter]
            
            # since prev was on hold, put prev back in
            if prev and prev[0] < 0:
                heappush(max_heap, prev)
                
            curr_freq+=1
            
            # now put the letter that we just inserted on hold
            prev = [curr_freq, curr_letter]
        
        res = ''.join(res)
        return res if len(res)==len(s) else ""