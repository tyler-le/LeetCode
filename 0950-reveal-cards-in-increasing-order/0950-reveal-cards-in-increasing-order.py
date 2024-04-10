class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        n = len(deck)
        deck.sort() # start from sorted position and perform the simulation
        indices = deque([x for x in range(n)])
        res = [None for _ in range(n)]
        
        for card in deck:
            
            # reveal this card
            res[indices.popleft()] = card
            
            # move this card to the end
            if indices:
                indices.append(indices.popleft())
        
        return res