class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        hmap_s_t = defaultdict(str)
        hmap_t_s = defaultdict(str)
        
        for s1, t1 in zip(s, t):
            # check if the mapping for s1 -> t1 is invalid
            if s1 in hmap_s_t and hmap_s_t[s1] != t1: 
                return False
            
            # check if the mapping for t1 -> s1 is invalid
            if t1 in hmap_t_s and hmap_t_s[t1] != s1: 
                return False
            
            # add it to both 
            hmap_s_t[s1] = t1
            hmap_t_s[t1] = s1
                
        return True
        
        