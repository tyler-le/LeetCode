class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # even positions should be sorted in increasing order
        n = len(deck)
        deck.sort()
        indices = deque([x for x in range(n)])
        res = [0 for _ in range(n)]
        
        for card in deck:
            res[indices.popleft()] = card
            
            if indices:
                indices.append(indices.popleft())
        
        return res