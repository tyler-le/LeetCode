class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s, hmap, idx = s.split(" "), collections.defaultdict(str), 0
        if len(s) != len(pattern): return False
        
        for p in pattern:
            if p not in hmap: 
                hmap[p] = s[idx]
            else: 
                if s[idx] != hmap[p]: return False
            idx+=1
            
        return False if len(set(hmap.values())) != len(hmap) else True
                