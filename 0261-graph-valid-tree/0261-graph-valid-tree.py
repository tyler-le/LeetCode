class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        q = deque([(0, -1)]) # (node, prev)
        visited.add(0)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while q:
            popped, prev = q.popleft()

            for nbor in graph[popped]:
                if nbor == prev: continue
                if nbor in visited: return False
                visited.add(nbor)
                q.append((nbor, popped))

        
        return len(visited) == n

        

