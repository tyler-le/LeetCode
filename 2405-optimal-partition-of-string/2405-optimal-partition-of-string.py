class Solution:
    def partitionString(self, s: str) -> int:
        count = set()
        out, l = 0, 0
        
        for r in range(len(s)):
            if s[r] in count:
                out+=1
                count.clear()
                l = r
                count.add(s[l])
            else:
                count.add(s[r])
                
        out+=1
        return out
                