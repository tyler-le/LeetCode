class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        res = float("inf")
        n = len(cards)
        hmap = defaultdict(int)
        
        for r in range(n):
            hmap[cards[r]]+=1
            
            while hmap[cards[r]] == 2:
                res = min(res, r-l+1)
                hmap[cards[l]]-=1
                l+=1
                
            
        return res if res != float("inf") else -1 