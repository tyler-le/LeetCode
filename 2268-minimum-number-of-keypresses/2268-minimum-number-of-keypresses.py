class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, count, max_heap = 0, Counter(s), []
        max_heap = [(-v, k) for k,v in Counter(s).items()]
        heapify(max_heap)
        
        # most freq go in first position
        # populate numpad (i//9) decides the order in a specific key location
        for i in range(len(max_heap)):
            freq, char = heappop(max_heap)
            # map to a key location and calc how many presses needed for this char
            res+=(((i//9) + 1) * -freq)
            
        return res
            
            