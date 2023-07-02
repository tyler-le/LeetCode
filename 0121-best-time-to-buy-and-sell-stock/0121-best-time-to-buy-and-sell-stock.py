class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        res = 0
        
        for i in range(1, len(prices)):
            curr_min = min(curr_min, prices[i])
            res = max(res, prices[i] - curr_min)
        
        return res
            
            
            
            