class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # sliding window, contract window when we exceed the max cost
        # record the max length substring
        
        res = 0
        l = 0
        n = len(s)
        curr = 0
        
        for r in range(n):
            curr+=(abs(ord(s[r]) - ord(t[r])))
            
            while curr > maxCost:
                curr-=(abs(ord(s[l]) - ord(t[l])))
                l+=1
            
            if curr <= maxCost:
                res = max(res, r-l+1)
        
        return res