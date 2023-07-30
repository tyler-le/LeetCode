class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log.startswith("../"):
                if res > 0:
                    res-=1
            elif log.startswith("./"):
                res+=0
            else:
                res+=1
        return max(0, res)