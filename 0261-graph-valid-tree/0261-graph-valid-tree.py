class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        q = deque([(0, -1)]) # (node, prev)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while q:
            popped, prev = q.popleft()
            if popped in visited: return False
            visited.add(popped)

            for nbor in graph[popped]:
                if nbor == prev: continue
                q.append((nbor, popped))

        
        return len(visited) == n

        

