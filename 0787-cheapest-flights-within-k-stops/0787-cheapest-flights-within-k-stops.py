from collections import defaultdict, deque
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Convert to adjacency list
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (node, weight, steps)
        q = deque([(src, 0, -1)])
        
        # Node: distance from src map
        distances = [math.inf] * n
        
        while q:
            popped_node, popped_dist, popped_steps = q.popleft()
            
            # Update distance only if it's less than the current distance
            if popped_dist < distances[popped_node]:
                distances[popped_node] = popped_dist
                
                # Explore neighbors
                for nbor, weight in graph[popped_node]:
                    if popped_steps < k and popped_dist + weight < distances[nbor]:
                        q.append((nbor, popped_dist + weight, popped_steps + 1))
        
        return distances[dst] if distances[dst] != math.inf else -1
