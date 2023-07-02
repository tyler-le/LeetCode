class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        res = 0
        
        for i in range(1, len(prices)):
            res = max(res, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
        
        return res
            
            
            
            