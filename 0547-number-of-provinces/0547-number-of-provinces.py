class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        
        def dfs(u):
            for v in range(n):
                if isConnected[u][v] == 1:
                    isConnected[u][v] = 0
                    isConnected[v][u] = 0
                    dfs(v)

        for i in range(n):
            if isConnected[i][i] == 1:
                res+=1
                dfs(i)

        return res
            