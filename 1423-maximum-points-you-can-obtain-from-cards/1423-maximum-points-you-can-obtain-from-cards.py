class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # find the minimum window of size n-k
        # subtract from sum(cardPoints)
        
        total = sum(cardPoints)
        
        l, n = 0, len(cardPoints)
        mini = float("inf")
        curr_sum = 0
        
        for r in range(n):
            curr_sum+=cardPoints[r]
            while (r-l+1) > (n-k):
                curr_sum-=cardPoints[l]
                l+=1
            if r-l+1 == n-k:
                mini = min(mini, curr_sum)
        
        return total - mini
            