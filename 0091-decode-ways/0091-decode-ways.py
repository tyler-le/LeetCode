class Solution:
    def numDecodings(self, s: str) -> int:
        
        # f(x) is the number of ways to decode x

        @cache
        def f(x):
            print(x)
            if not x: return 1
            if len(x) == 1: 
                if x == "0": return 0
                else: return 1

            res = 0

            # take x[0] and recurse on x[1:]
            first, rest = x[0], x[1:]
            if 1 <= int(first) <= 26 and not (len(first) == 2 and first[0] == "0"): 
                res += f(rest)

            # tale x[0:2] and recurse on x[2:]     
            first, rest = x[0:2], x[2:]   
            if 1 <= int(first) <= 26 and not (len(first) == 2 and first[0] == "0"): 
                res += f(rest)

            return res    
        
        return f(s)
