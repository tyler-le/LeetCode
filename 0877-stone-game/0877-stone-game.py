class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def f(i, j, alice_turn):
            if i > j: return 0
            
            first, second = -math.inf, -math.inf

            # take piles[i]
            if alice_turn: first = piles[i] + f(i+1, j, not alice_turn)
            else: first = -piles[i] + f(i+1, j, not alice_turn)

            # take piles[j]
            if alice_turn: second = piles[j] + f(i, j-1, not alice_turn)
            else: second = -piles[j] + f(i, j-1, not alice_turn)

            return max(first, second) if alice_turn else min(first, second)

        return f(0, len(piles) - 1, True) > 0