class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        @cache
        def f(index, target):
            if index >= n: return 0
            if target < 0: return 0
            if target == 0: return 1

            res = 0

            # use this coin
            res+=f(index, target - coins[index])

            # skip this coin
            res+=f(index + 1, target)
    

            
            return res

        return f(0, amount)
