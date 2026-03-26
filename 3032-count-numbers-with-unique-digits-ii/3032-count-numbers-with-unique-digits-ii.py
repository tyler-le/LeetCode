class Solution:
    def numberCount(self, a: int, b: int) -> int:
        # f(a,b) = f(b) - f(a-1)

        def f(x):
            if x == 0: return 0
            if x == 1: return 1
            
            res = 0
            s = str(x)

            res += f(x-1) + (len(set(s)) == len(s))
            return res
        
        return f(b) - f(a-1)

    

