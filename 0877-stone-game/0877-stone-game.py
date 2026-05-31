class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        alice, bob = 0, 0
        l, r = 0, len(piles) - 1
        parity = True

        while l <= r:
            if parity:
                if piles[l] < piles[r]:
                    alice+=piles[r]
                    r-=1
                else:
                    alice+=piles[l]
                    l+=1
            else:
                if piles[l] < piles[r]:
                    bob+=piles[r]
                    r-=1
                else:
                    bob+=piles[l]
                    l+=1

        return alice > bob