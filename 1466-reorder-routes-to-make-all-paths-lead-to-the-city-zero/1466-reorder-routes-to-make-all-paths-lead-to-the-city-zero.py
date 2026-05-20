class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        def dfs(prev, curr):
            out = 0

            if prev is not None and (prev, curr) in connections:
                out+=1

            for nbor in graph[curr]:
                if nbor == prev: continue
                out+=dfs(curr, nbor)
            
            return out


        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        connections = set([tuple(x) for x in connections])
        return dfs(None, 0)