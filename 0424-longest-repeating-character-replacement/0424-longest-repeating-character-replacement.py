class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num_replacements_left = k
        l = 0
        res = 0
        n = len(s)
        hmap = defaultdict(int)
        
        for r in range(n):
            hmap[s[r]]+=1
            
            while (r-l+1 - max(hmap.values())) > k:
                hmap[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
            
        
        return res
            