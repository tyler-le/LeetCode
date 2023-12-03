class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        hmap_s_t = defaultdict(str)
        hmap_t_s = defaultdict(str)
        res = ""
        
        for s1, t1 in zip(s, t):
            if (s1 not in hmap_s_t) and (t1 not in hmap_t_s):
                hmap_s_t[s1] = t1
                hmap_t_s[t1] = s1
                
            elif hmap_s_t[s1] != t1 or hmap_t_s[t1] != s1: 
                return False
        
        return True
        
        