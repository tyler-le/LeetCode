class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        num_evens, num_odds = 0, 0
        res = 0
        for pos in position:
            if pos % 2 == 0: num_evens+=1
            else: num_odds +=1
        
        if not num_evens or not num_odds: return 0
        elif num_evens < num_odds: return num_evens
        else: return num_odds
            
            