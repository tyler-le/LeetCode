class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros_seen = 0
        res = 0

        for ch in s:
            if ch == "0":
                res+=zeros_seen
            else:
                zeros_seen+=1
        
        return res
