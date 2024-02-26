class Solution:
    def minFlips(self, target: str) -> int:
        res, state = 0, "0"
        
        for ch in target:
            if not (state == ch):
                res+=1
                state = "1" if state == "0" else "0"
                
        return res