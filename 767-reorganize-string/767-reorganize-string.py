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
        prev = None
        
        while max_heap:
            popped = heappop(max_heap)
            freq, letter = popped[0], popped[1]
            res += [letter]
            
            if prev and prev[0] < 0:
                heappush(max_heap, prev)
                
            freq+=1
            prev = [freq, letter]
            heappush(prev, max_heap)
        
        res = ''.join(res)
        return res if len(res)==len(s) else ""