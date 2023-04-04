class Solution:
    def partitionString(self, s: str) -> int:
        hmap = collections.defaultdict(int)
        out = []
        l = 0
        
        for r in range(len(s)):
            if hmap[s[r]] > 0:
                out.append(s[l:r])
                hmap.clear()
                l = r
                hmap[s[l]]+=1
            else:
                hmap[s[r]]+=1
                
        print(out)
        return len(out)+1
                