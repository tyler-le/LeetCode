class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        res = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        
        # For each result value at A[i][j], we greedily take the min(row[i], col[j]).
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i]-=res[i][j]
                colSum[j]-=res[i][j]
        
        return res