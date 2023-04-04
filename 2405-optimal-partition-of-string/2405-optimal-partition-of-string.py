class Solution:
    def partitionString(self, s: str) -> int:
        hmap = collections.defaultdict(int)
        out = 0
        l = 0
        
        for r in range(len(s)):
            if hmap[s[r]] > 0:
                out+=1
                hmap.clear()
                l = r
                hmap[s[l]]+=1
            else:
                hmap[s[r]]+=1
                
        out+=1
        return out
                