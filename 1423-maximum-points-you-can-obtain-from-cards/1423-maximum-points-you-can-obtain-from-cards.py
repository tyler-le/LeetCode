class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, curr_sum, res = 0, 0, -float("inf")
        sumi, n = sum(cardPoints), len(cardPoints)
        
        for r in range(n):
            curr_sum+=cardPoints[r]
            
            while (r - l + 1) > (n - k):
                curr_sum-=cardPoints[l]
                l+=1
                
            if (r - l + 1) == (n - k):   
                res = max(res, sumi - curr_sum)
        
        return res