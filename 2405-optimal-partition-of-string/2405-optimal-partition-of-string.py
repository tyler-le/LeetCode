class Solution:
    def partitionString(self, s: str) -> int:
        count = set()
        out = 0
        
        for i in range(len(s)):
            if s[i] in count:
                out+=1
                count.clear()
                
            count.add(s[i])
                
        out+=1
        return out
                