class Solution:
    def minPartitions(self, n: str) -> int:
        
        res = 0
        for ch in n:
            res = max(res, int(ch))
        return res