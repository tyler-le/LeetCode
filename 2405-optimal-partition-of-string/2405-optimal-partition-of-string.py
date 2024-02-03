class Solution:
    def partitionString(self, s: str) -> int:
        l = 0
        res = 0
        n = len(s)
        hmap = defaultdict(int)
        
        for r in range(n):
            if hmap[s[r]] == 1:
                res+=1
                l = r
                hmap = defaultdict(int)
                hmap[s[r]]+=1
            else:
                hmap[s[r]]+=1
            
                
        return res + max(hmap.values())
            
            
            