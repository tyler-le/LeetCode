class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        edge_set = set([(u,v) for u, v in connections])
        res = 0

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([0])
        visited = set([0])

        while q: 
            popped = q.popleft()

            for nbor in graph[popped]:
                if nbor in visited: continue
                visited.add(nbor)
                q.append(nbor)
                if (popped, nbor) in edge_set:
                    res+=1

        return res