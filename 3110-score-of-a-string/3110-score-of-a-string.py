class Solution:
    def scoreOfString(self, s: str) -> int:
        # sliding window of length 2
        
        res = 0
        n = len(s)
        for i in range(n-1):
            curr = abs(ord(s[i]) - ord(s[i+1]))
            res+=curr
        return res