class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        inverted_graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        n = len(graph)
        res = []
        safe = defaultdict(bool)

        for i in range(n):
            for nbor in graph[i]:
                inverted_graph[nbor].append(i)
                indegrees[i]+=1

        for node in range(n):
            if not indegrees[node]:
                q.append(node)
                safe[node] = True
        
        while q:
            popped_node = q.popleft()

            for nbor in inverted_graph[popped_node]:
                indegrees[nbor]-=1
                if not indegrees[nbor]:
                    q.append(nbor)
                    safe[nbor] = True

        for i in range(n):
            if safe[i]: res.append(i)
            
        return res
        



        