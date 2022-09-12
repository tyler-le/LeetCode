"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        old2new = {}
        
        def dfs(node):
            if not node: return None
            if node in old2new: return old2new[node]
            
            old2new[node] = Node(node.val)
            
            for nbor in node.neighbors:
                old2new[node].neighbors.append(dfs(nbor))
            
            return old2new[node]
        
        dfs(node)       
        return old2new[node] if node else None