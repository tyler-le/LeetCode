class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n1_dist = {}
        n2_dist = {}
        graph = defaultdict(list)
        res = (math.inf, -1)
        n = len(edges)

        def bfs(source, dist_map):
            visited = set()
            visited.add(source)
            q = deque([(source, 0)])
            dist_map[source] = 0

            while q:
                popped_node, popped_dist = q.popleft()

                for nbor in graph[popped_node]:
                    if nbor in visited: continue
                    visited.add(nbor)
                    dist_map[nbor] = popped_dist + 1
                    q.append((nbor, popped_dist + 1))


        for u in range(len(edges)):
            v = edges[u]
            graph[u].append(v)
        
        bfs(node1, n1_dist)
        bfs(node2, n2_dist)
        
        for node in range(n):
            first = n1_dist[node] if node in n1_dist else math.inf
            second = n2_dist[node] if node in n2_dist else math.inf

            if max(first, second) < res[0]:
                res = (max(first, second), node)
            
        return res[1]
        
        
