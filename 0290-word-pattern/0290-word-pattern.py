class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern): return False
        hmap = collections.defaultdict(str)
        idx = 0
        for p in pattern:
            if p not in hmap:
                hmap[p] = s[idx]
            else:
                if s[idx] != hmap[p]: 
                    return False
            idx+=1
        if len(set(hmap.values())) != len(hmap): return False
        return True
                