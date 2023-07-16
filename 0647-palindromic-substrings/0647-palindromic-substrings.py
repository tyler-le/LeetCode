class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        
        def helper(i):
            count = 0
            
            # odd length palindromes
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            
            # even length palindromes
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            
            return count
            
        for i in range(n):
            res+=helper(i)
        
        return res
            
                
        