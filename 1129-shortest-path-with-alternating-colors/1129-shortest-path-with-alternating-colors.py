class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = deque([(0, None, 0)]) # node, prev_color, dist

        graph = defaultdict(list)
        distances = {}
        visited = set((0, None)) # (node, edge_color)
        res = []

        for u, v in redEdges:
            graph[u].append((v, "red"))
        
        for u, v in blueEdges:
            graph[u].append((v, "blue"))

        while q:
            popped_node, prev_color, popped_dist = q.popleft()
            
            for nbor_node, edge_color in graph[popped_node]:
                if edge_color == prev_color: continue
                if (nbor_node, edge_color) in visited: continue
                
                q.append((nbor_node, edge_color, popped_dist + 1))
                if nbor_node not in distances:
                    distances[nbor_node] = popped_dist + 1
                visited.add((nbor_node, edge_color))
        

        for i in range(n):
            if i == 0: res.append(0)
            elif i not in distances: res.append(-1)
            else: res.append(distances[i])
        
        return res

        