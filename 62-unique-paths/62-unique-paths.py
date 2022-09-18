class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # calculate n choose k directly
        
        # we have m-1 'right' moves and n-1 'down' moves
        # hence (m-1) + (n-1) Choose n
        return comb((m-1) + (n-1), n-1)