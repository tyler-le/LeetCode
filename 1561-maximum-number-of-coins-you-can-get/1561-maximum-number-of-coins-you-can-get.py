class Solution:
    def maxCoins(self, piles: List[int]) -> int:

            
        piles.sort()
        l, r = 0, len(piles) - 2
        res = 0
        while l < r:
            res+=piles[r]
            r-=2
            l+=1
        
        return res