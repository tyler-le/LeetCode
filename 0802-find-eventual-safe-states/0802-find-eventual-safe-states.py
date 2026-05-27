class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # topological sort - prune off leaves

        n = len(graph)
        indegrees = defaultdict(int)
        inverted = defaultdict(list)
        q = deque()
        res = []

        for u in range(n):
            for v in graph[u]:
                inverted[v].append(u)
                indegrees[u]+=1            

        for node in range(n):
            if not indegrees[node]:
                q.append(node)
                res.append(node)

        while q:
            popped_node = q.popleft()
            for nbor in inverted[popped_node]:
                indegrees[nbor]-=1
                if not indegrees[nbor]:
                    q.append(nbor)
                    res.append(nbor)

        return [i for i in range(n) if indegrees[i] == 0]
