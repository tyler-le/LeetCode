class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices
        stack = []
        
        for i, price in enumerate(prices):
            
            while stack and price <= stack[-1][0]:
                popped_price, popped_index = stack.pop()
                res[popped_index] = (popped_price - price)
            
            stack.append((price, i))
        
        return res