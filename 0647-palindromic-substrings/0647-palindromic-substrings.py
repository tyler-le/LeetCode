class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # "is s[i...j] a palindrome?"
        cache = {}
        def f(i, j):
            if i >= j: return True
            if (i, j) in cache: return cache[i, j]
            
            inner_res = f(i+1, j-1)

            if s[i] == s[j] and inner_res: 
                cache[(i, j)] = True
                return True

            cache[(i, j)] = False
            return False

        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i, n):
                if f(i, j):
                    res+=1
        
        return res