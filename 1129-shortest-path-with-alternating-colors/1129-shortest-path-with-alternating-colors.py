class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list) # [(nbor, edge_color)]
        q = deque([(0, 0, None)]) # (node, dist, prev_edge_color)
        RED, BLUE = 0, 1
        answer = [-1 for _ in range(n)]
        answer[0] = 0
        visited = set() # (node, incoming color edge)

        for u, v in redEdges:
            graph[u].append((v, RED))

        for u, v in blueEdges:
            graph[u].append((v, BLUE))

    
        while q:
            popped_node, popped_dist, prev_edge_color = q.popleft()

            for nbor, edge_color in graph[popped_node]:
                if prev_edge_color == edge_color: continue
                if (nbor, edge_color) in visited: continue

                q.append((nbor, popped_dist + 1, edge_color))
                visited.add((nbor, edge_color))
                if answer[nbor] == -1: answer[nbor] = popped_dist + 1

        return answer
                

        