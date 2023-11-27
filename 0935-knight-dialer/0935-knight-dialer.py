class Solution:
    def knightDialer(self, n: int) -> int:

        res = 0
        dp = dict()
        possible_jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        def rec(i, j):
            if i == 0: return 1
            if (i, j) in dp: return dp[(i,j)]
            
            acc = 0
        
            # explore all combinations from current square
            for pj in possible_jumps[j]:
                acc+=rec(i-1, pj) % (10**9 + 7)

            dp[(i,j)] = acc 
            return acc
        
        for sq in range(10):
            res += rec(n - 1, sq) % (10**9 + 7)
            
        return res % (10**9 + 7)
            