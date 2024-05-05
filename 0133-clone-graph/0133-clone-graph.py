"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        
        def dfs(node):
            
            if not node: return None
            if node in hmap: return hmap[node]
            
            copy = Node(node.val)
            hmap[node] = copy
            
            for nbor in node.neighbors:
                copy.neighbors.append(dfs(nbor))
            
            return hmap[node]
        
        return dfs(node)
         