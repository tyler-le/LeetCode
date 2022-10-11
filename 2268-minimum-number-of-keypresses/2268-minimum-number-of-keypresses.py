class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, count, max_heap = 0, Counter(s), []
        
        for ch, freq in count.items():
            max_heap.append((-freq, ch))
            
        heapify(max_heap)
        
        # most freq go in first position
        for i in range(len(max_heap)):
            freq, char = heappop(max_heap)
            res+=(((i//9) + 1) * -freq)
            
        return res
            
            