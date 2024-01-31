"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        hmap = {}
        
        def dfs(node):
            if not node: return None
            if node in hmap: return hmap[node]
            copy = Node(node.val)
            hmap[node] = copy
            for ch in node.children:
                copy.children.append(dfs(ch))
            return copy
        return dfs(root)