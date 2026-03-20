class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        if not s: return True

        for ch in t: 
            if ch == s[p1]:
                p1+=1
        
            if p1 == len(s):
                return True
        
        return False