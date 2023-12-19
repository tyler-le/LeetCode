class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = 0

        for ch in t:
            if s1 == len(s): return True
            if ch == s[s1]: s1+=1
        
        return s1 == len(s)