class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        max_heap = [[-count, char] for char, count in count.items()]
        heapify(max_heap)
        
        res = ""
        prev = None
        while max_heap or prev:
            
            if prev and not max_heap:
                return ""
            
            count, char = heappop(max_heap)
            res += char
            count += 1 # because it's negative
            
            if prev:
                heappush(max_heap, prev)
                prev = None
                
            if count != 0:
                prev = [count, char]

        return res
            
            
