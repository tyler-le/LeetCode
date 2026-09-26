class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        
        @cache
        def f(index, can_buy, count):
            res = -math.inf

            if count == 2: return 0
            
            if index >= n:
                if count <= 2:
                    if can_buy: return 0
                    else: return -math.inf
                else: return -math.inf
                
            if can_buy:
                buy = -prices[index] + f(index + 1, False, count)
                hold = f(index + 1, True, count)
                res = max(res, buy, hold)
            
            else:
                sell = prices[index] + f(index + 1, True, count + 1)
                hold = f(index + 1, False, count)
                res = max(res, sell, hold)
                
            return res
        
        return f(0, True, 0)