class Solution:
    def coloredCells(self, n: int) -> int:
        
        # @cache
        # def f(i):
        #     if i == 1: return 1
        #     return f(i-1) + (4*(i-1))
        
        # return f(n)

        if n == 1: return 1
        return int(1 + (4 * ( (n-1) * (n) / 2 )))