class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if we encounter a lower buying day, buy on that lower day

        buy, res, n = math.inf, 0, len(prices)

        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            
            res = max(res, prices[i] - buy)
        
        return res

