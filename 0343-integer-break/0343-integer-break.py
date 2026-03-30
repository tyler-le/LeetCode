class Solution:
    def integerBreak(self, n: int) -> int:
        

        cache = {}
        def f(x):
            if x <= 0: return 0

            if x in cache: return cache[x]

            res = 0

            for i in range(1, x):
                res = max(res, i * f(x - i))
                res = max(res, i * (x-i))
            
            cache[x] = res
            return res
        
        return f(n)