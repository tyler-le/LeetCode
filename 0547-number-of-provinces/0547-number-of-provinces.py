class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        graph = defaultdict(set)
        res = 0
        visited = set()
        
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for u in list(graph[node]):
                dfs(u)     
        
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    graph[r+1].add(c+1)
                    graph[c+1].add(r+1)
        
        for i in range(1, n+1):
            if i not in visited:
                res+=1
                dfs(i)
        
        return res