class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        if not len(s): return True
        for ch in t:
            
            if ch == s[ptr]:
                ptr+=1
        
            if ptr == len(s): 
                return True
            
        return False
            