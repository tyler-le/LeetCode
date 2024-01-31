class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        cnt = 0
        res = 0
        
        for w in sorted(weight):
            cnt+=w
            if cnt > 5000: 
                return res
            res+=1
        
        return res