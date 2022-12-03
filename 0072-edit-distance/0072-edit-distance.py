class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        INF = float('inf')
        
        # create a n x m matrix of infinities
        
        A = [[INF for x in range(m+1)] for y in range(n+1)] 
        
        for row in range(n+1): A[row][0] = row
            
        for col in range(m+1): A[0][col] = col

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                     A[i][j] = min(0+A[i-1][j-1], 1+A[i-1][j], 1+A[i][j-1])
                else:
                    A[i][j] = min(1+A[i-1][j-1], 1+A[i-1][j], 1+A[i][j-1])
                    
        return A[-1][-1]
                    