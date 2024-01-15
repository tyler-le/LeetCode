class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        lose = defaultdict(int)
        players = set()
        res = [[], []]
        
        for winner, loser in matches:
            lose[loser]+=1
            players.add(winner)
            players.add(loser)
            
        for p in list(players):
            if lose[p] == 0: res[0].append(p)
            elif lose[p] == 1: res[1].append(p)
               
        res[0].sort()
        res[1].sort()
        return res
            
        