class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        if len(pattern) != len(s): return False
        
        # map pattern -> string
        p_to_s = {}
        s_to_p = {}
        
        
        for p1, s1 in zip(pattern, s):
            if p1 in p_to_s and p_to_s[p1] != s1: return False
            if s1 in s_to_p and s_to_p[s1] != p1: return False
            if p1 not in p_to_s: p_to_s[p1] = s1
            if s1 not in s_to_p: s_to_p[s1] = p1
                
        return True
            