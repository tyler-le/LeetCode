class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        res = money - (prices[0] + prices[1])
        
        return res if res >= 0 else money