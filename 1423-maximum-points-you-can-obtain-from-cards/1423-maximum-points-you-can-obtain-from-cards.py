class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total_points = sum(cardPoints)
        window_size = len(cardPoints) - k
        curr_sum = 0
        l=0
        res = 0
        for r in range(len(cardPoints)):
            curr_sum += cardPoints[r]
            if r-l+1 > window_size:
                curr_sum -= cardPoints[l]
                l+=1
                
            if r-l+1 == window_size:
                res = max(total_points - curr_sum, res)
                

        return res
            