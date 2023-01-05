class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m, res = len(strs), len(strs[0]), 0
        
        for i in range(m):
            for j in range(1, n):
                if ord(strs[j][i]) < ord(strs[j-1][i]):
                    res+=1
                    break
        return res