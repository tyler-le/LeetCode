class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        x, y = text1, text2
        n, m = len(x), len(y)
        
        A = [[0 for _ in range(m+1)] for _ in range(n+1)] 
        
        A[0][0] = 0
        
        for i in range (0, n): 
            for j in range(0, m):
                if x[i] == y[j]:
                    A[i+1][j+1] = 1 + A[i][j]
                else:
                    A[i+1][j+1] = max(A[i][j+1], A[i+1][j], A[i][j])
        print(A)   
        return A[n][m]