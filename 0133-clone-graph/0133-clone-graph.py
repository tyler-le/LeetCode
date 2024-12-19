"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # map node to clone
        clones = {}
        

        def dfs(node):
            if not node: return None
            if node in clones: return clones[node]

            clone = Node(node.val)
            clones[node] = clone

            for nbor in node.neighbors:
                clone.neighbors.append(dfs(nbor))

            return clone
            
        return dfs(node)
