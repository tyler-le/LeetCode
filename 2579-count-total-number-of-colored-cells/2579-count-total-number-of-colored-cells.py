class Solution:
    def coloredCells(self, n: int) -> int:
        
        # @cache
        # def f(i):
        #     if i == 1: return 1
        #     return f(i-1) + (4*(i-1))
        
        # return f(n)


        '''
        n = 1: 1
        n = 2: 1 + 4
        n = 3: 1 + 4 + 8
        n = 4: 1 + 4 + 8 + 12

        = 1 + sum from i=1 to n-1 (4i)
        = 1 + [ 4(1) + 4(2) + 4(3) + ... + 4(n-1]) ]
        = 1 + [ 4 (1 + 2 + ... + n-1) ]
        = the answer below
        '''
        if n == 1: return 1
        return int(1 + (4 * ( (n-1) * (n) / 2 )))