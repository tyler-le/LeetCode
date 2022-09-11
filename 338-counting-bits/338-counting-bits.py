class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def find_bits(n):
            res = 0
        
            while n != 0:
                if 1 & n: res += 1
                n = n >> 1
            
            return res
        
        res = []
        
        for i in range(0, n+1):
            num_ones = find_bits(i)
            res.append(num_ones)
        
        return res