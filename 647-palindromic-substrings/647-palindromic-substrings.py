class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def count(i):
            ans = 0
            
            # odd length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans+=1
                l-=1
                r+=1
                
            # even length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans+=1
                l-=1
                r+=1
            
            return ans
        
        
        res = 0
        
        for i in range(len(s)):
            res+=count(i)
        return res