class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        # two pass
        all_left, all_right = 0, 0
        
        # choose all left
        curr = 0
        for move in moves:
            if move == "R": curr+=1
            else: curr-=1
        all_left = curr

        # choose all right
        curr = 0
        for move in moves:
            if move == "L": curr-=1
            else: curr+=1
        all_right = curr

        return max(abs(all_left), abs(all_right))