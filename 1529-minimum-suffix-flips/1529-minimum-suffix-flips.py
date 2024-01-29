class Solution:
    def minFlips(self, target: str) -> int:
        status = "0"
        res = 0
        
        for ch in target:
            if ch != status:
                res+=1
                status = "0" if status == "1" else "1"
        
        return res