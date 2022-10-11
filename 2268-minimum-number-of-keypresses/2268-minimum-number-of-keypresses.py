class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        count = Counter(s)
        max_heap = []
        
        for k, v in count.items():
            max_heap.append((-v, k))
            
        heapify(max_heap)
        print(max_heap)
        
        # most freq go in first position
        for i in range(len(max_heap)):
            freq, char = heappop(max_heap)
            res+=(((i//9) + 1) * -freq)
            
        return res
            
            