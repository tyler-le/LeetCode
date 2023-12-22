class Solution:
    def maxScore(self, s: str) -> int:
        
        res = 0        
        left_score, right_score = 0, s.count("1")
        
        for i in range(len(s) - 1):
            if s[i] == "0":
                left_score+=1
            else:
                right_score-=1
            
            score = left_score + right_score
            res = max(res, score)
            
        return res
            