class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # sliding window
        # contract window when we exceed budget
        
        l = 0
        res = 0
        curr_cost = 0
        n = len(s)
        
        for r in range(n):
            curr_cost += abs(ord(s[r]) - ord(t[r]))
            
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            
            res = max(res, r-l+1)
        
        return res