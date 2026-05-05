class Solution:
    def coloredCells(self, n: int) -> int:
        def f(i):
            if i == 1: return 1
            return f(i-1) + (4*(i-1))
        
        return f(n)