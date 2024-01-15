class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losses = defaultdict(int)
        res = [[], []]
        
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser]+=1
            
        for player, count in losses.items():
            if losses[player] == 0: res[0].append(player)
            elif losses[player] == 1: res[1].append(player)
               
        res[0].sort()
        res[1].sort()
        return res
            
        