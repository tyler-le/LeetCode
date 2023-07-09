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
        hmap = dict()
        
        if not node: return None
        
        def dfs(node):
            hmap[node] = Node(node.val, [])
            for nbor in node.neighbors:
                if nbor not in hmap:
                    dfs(nbor)
                hmap[node].neighbors.append(hmap[nbor])

        dfs(node)
        return hmap[node]
    
    