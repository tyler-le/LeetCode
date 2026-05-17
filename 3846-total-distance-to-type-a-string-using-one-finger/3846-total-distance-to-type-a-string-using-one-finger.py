class Solution:
    def totalDistance(self, s: str) -> int:
        keyboard = [
            ["q","w","e","r","t","y","u","i","o","p"],
            ["a","s","d","f","g","h","j","k","l",""],
            ["z","x","c","v","b","n","m","","",""],
        ]

        n, m = len(keyboard), len(keyboard[0])
        hmap = {}

        for i in range(n):
            for j in range(m):
                hmap[(keyboard[i][j])] = (i,j)

        res = 0
        prev_x, prev_y = hmap["a"]
        for ch in s:
            curr_x, curr_y = hmap[ch]
            res+=(abs(prev_x - curr_x) + abs(prev_y - curr_y))
            prev_x, prev_y = curr_x, curr_y
        return res