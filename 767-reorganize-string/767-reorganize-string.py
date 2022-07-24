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
            freq, letter = popped[0], popped[1]
            res += [letter]
            
            # since prev was on hold, put prev back in
            if prev and prev[0] < 0:
                heappush(max_heap, prev)
                
            freq+=1
            
            # now put the letter that we just inserted on hold
            prev = [freq, letter]
        
        res = ''.join(res)
        return res if len(res)==len(s) else ""