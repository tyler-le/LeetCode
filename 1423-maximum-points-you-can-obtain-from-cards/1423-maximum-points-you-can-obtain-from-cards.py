class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sliding window of length n-k
        # minimize sum within window
        # produces maximum sum of length k outside window 
        
        n = len(cardPoints)
        window_size = n-k
        res = math.inf
        sumi = sum(cardPoints)
        l = 0
        curr = 0
        
        for r in range(n):
            curr+=cardPoints[r]
            
            if r-l+1 > window_size:
                curr-=cardPoints[l]
                l+=1
            
            if r-l+1 == window_size:
                res = min(res, curr)
        
        return sumi - res