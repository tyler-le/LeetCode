class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        
        for x in details:
            if int(x[11:13]) > 60: res+=1
        
        return res