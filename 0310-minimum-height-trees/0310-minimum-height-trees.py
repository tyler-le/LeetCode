class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        visited = set()

        if not edges: return [i for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegrees[u]+=1
            indegrees[v]+=1
        
        for node, indegree in indegrees.items():
            if indegree == 1:
                q.append(node)
                visited.add(node)

        
        while n > 2:
            level_size = len(q)
            n-=level_size

            for _ in range(level_size):
                popped = q.popleft()
                for nbor in graph[popped]:
                    if nbor in visited: continue
                    indegrees[nbor]-=1
                    if indegrees[nbor] == 1:
                        q.append(nbor)
                        visited.add(nbor)
        
        return list(q)

       