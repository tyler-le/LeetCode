class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:        
        
        l = 0
        n = len(s)
        hmap = defaultdict(int)
        res = 0
        
        for r in range(n):
            hmap[s[r]]+=1
            
            while hmap[s[r]] > 1:
                hmap[s[l]]-=1
                l+=1
            
            res += (r-l+1)
                
        return res
            