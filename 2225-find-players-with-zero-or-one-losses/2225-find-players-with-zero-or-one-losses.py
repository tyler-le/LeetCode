class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        win_count, lose_count = defaultdict(int), defaultdict(int)
        min_player, max_player = math.inf, -math.inf

        for winner, loser in matches:
            win_count[winner]+=1
            lose_count[loser]+=1
            min_player = min(min_player, winner, loser)
            max_player = max(max_player, winner, loser)
        
        for player in range(min_player, max_player + 1):

            # this player did not play
            if player not in win_count and player not in lose_count:
                continue

            # all players that have not lost any matches.
            if player not in lose_count:
                res[0].append(player)

            # all players that have lost exactly one match.
            if lose_count[player] == 1:
                res[1].append(player)
        
        return res


