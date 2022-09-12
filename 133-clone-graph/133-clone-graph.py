"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    # BFS
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        q = deque([node])
        visited = {node: Node(node.val)}
        
        while q:
            popped = q.popleft()
            
            for nbor in popped.neighbors:
                if nbor in visited:
                    visited[popped].neighbors.append(visited[nbor])
                else:
                    visited[nbor] = Node(nbor.val)
                    visited[popped].neighbors.append(visited[nbor])       
                    q.append(nbor)
                    
                
        return visited[node] 
        