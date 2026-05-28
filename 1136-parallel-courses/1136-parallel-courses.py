class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        visited = set()

        for u, v in relations:
            graph[u].append(v)
            indegrees[v]+=1

        for node in range(1, n+1):
            if not indegrees[node]:
                q.append(node)
                visited.add(node)

        while q:
            level_size = len(q)
            res+=1

            for _ in range(level_size):
                popped = q.popleft()
                
                for nbor in graph[popped]:
                    indegrees[nbor]-=1
                    if not indegrees[nbor]:
                        q.append(nbor)
                        visited.add(nbor)

        return res if len(visited) == n else -1

        
        