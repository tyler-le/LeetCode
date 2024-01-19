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
        # map node : copy
        hmap = {}
        
        def dfs(curr):
            if not curr: return None
            if curr in hmap: return hmap[curr]
            
            copy = Node(curr.val)
            hmap[curr] = copy
            nbors = []
            
            for nbor in curr.neighbors:
                copy.neighbors.append(dfs(nbor))
            
            return copy
            
        return dfs(node)